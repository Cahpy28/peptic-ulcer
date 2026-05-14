from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import ChatbotForm, EmailCodeVerificationForm, PatientAssessmentForm, PatientRegistrationForm, PUDDatasetUploadForm, SymptomLogForm
from .data_services import fetch_openfda_warnings, fetch_pubmed_references, process_pud_dataset_upload
from .decorators import verified_login_required
from .email_verification import send_verification_email, verify_code, verify_token
from .ml import chatbot_guidance, simulated_xgboost_prediction, symptom_log_risk
from .models import Assessment, Patient, PUDDatasetUpload, SymptomLog


def landing(request):
    return render(request, "patients/landing.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("patients:dashboard")

    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_verification_email(request, user)
            request.session["pending_verification_email"] = user.email
            messages.success(request, "Verification code and link sent to your email.")
            return redirect("patients:verification_sent")
    else:
        form = PatientRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def verification_sent(request):
    initial_email = request.session.get("pending_verification_email", "")
    if request.method == "POST":
        form = EmailCodeVerificationForm(request.POST)
        if form.is_valid():
            user, error = verify_code(form.cleaned_data["email"], form.cleaned_data["code"])
            if user:
                user.is_active = True
                user.save(update_fields=["is_active"])
                request.session.pop("pending_verification_email", None)
                login(request, user)
                messages.success(request, "Account created successfully.")
                return redirect("patients:dashboard")
            form.add_error("code", error)
    else:
        form = EmailCodeVerificationForm(initial={"email": initial_email})
    return render(
        request,
        "registration/verification_sent.html",
        {"form": form, "pending_email": initial_email, "show_verification_modal": bool(initial_email)},
    )


def verify_email(request, uidb64, token):
    user = verify_token(uidb64, token)
    if not user:
        messages.error(request, "Verification link expired or invalid")
        return render(request, "registration/verification_invalid.html", status=400)
    user.is_active = True
    user.save(update_fields=["is_active"])
    request.session.pop("pending_verification_email", None)
    login(request, user)
    messages.success(request, "Account created successfully.")
    return redirect("patients:dashboard")


def resend_verification(request):
    if request.method != "POST":
        return redirect("login")
    email = request.POST.get("email", "").strip().lower()
    User = get_user_model()
    user = User.objects.filter(email__iexact=email, is_active=False).first()
    if user:
        send_verification_email(request, user)
        request.session["pending_verification_email"] = user.email
    messages.success(request, "A fresh verification code and link have been sent.")
    return redirect("patients:verification_sent")


@verified_login_required
def dashboard(request):
    assessments = Assessment.objects.select_related("patient").filter(patient__user=request.user)[:8]
    symptom_logs = SymptomLog.objects.filter(user=request.user)[:10]
    latest_assessment = assessments.first()
    latest_log = symptom_logs.first()
    return render(
        request,
        "patients/dashboard.html",
        {
            "assessments": assessments,
            "symptom_logs": symptom_logs,
            "latest_assessment": latest_assessment,
            "latest_log": latest_log,
        },
    )


@verified_login_required
def assessment_create(request):
    prediction = None
    if request.method == "POST":
        form = PatientAssessmentForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.create(
                user=request.user,
                patient_code=f"PUD-{request.user.id}-{timezone.now().strftime('%H%M%S')}",
                full_name=form.cleaned_data["full_name"],
                age=form.cleaned_data["age"],
                gender=form.cleaned_data["gender"],
                phone=form.cleaned_data["phone"],
            )
            latest_dataset = PUDDatasetUpload.objects.filter(user=request.user, status="processed").first()
            dataset_profile = latest_dataset.column_profile if latest_dataset else None
            references = fetch_pubmed_references("peptic ulcer disease clinical guideline H pylori NSAID")
            warnings = fetch_openfda_warnings(form.cleaned_data.get("medications", ""))
            prediction = simulated_xgboost_prediction(form.cleaned_data, dataset_profile, references, warnings)
            assessment = Assessment.objects.create(
                patient=patient,
                systolic_bp=form.cleaned_data.get("systolic_bp"),
                diastolic_bp=form.cleaned_data.get("diastolic_bp"),
                weight=form.cleaned_data.get("weight"),
                pain_severity=form.cleaned_data["pain_severity"],
                hpylori_status=form.cleaned_data["hpylori_status"],
                nsaid_use=form.cleaned_data["nsaid_use"],
                bleeding_symptoms=form.cleaned_data["bleeding_symptoms"],
                smoking_history=form.cleaned_data["smoking_history"],
                alcohol_intake=form.cleaned_data["alcohol_intake"],
                stress_level=form.cleaned_data["stress_level"],
                diet_pattern=form.cleaned_data["diet_pattern"],
                previous_ulcer=form.cleaned_data["previous_ulcer"],
                diagnosis=form.cleaned_data.get("diagnosis", ""),
                medications=form.cleaned_data.get("medications", ""),
                complications=form.cleaned_data.get("complications", ""),
                symptoms=form.cleaned_data["symptoms"],
                risk_score=prediction["risk_score"],
                severity=prediction["severity"],
                feature_importance=prediction["feature_importance"],
                recommendations=prediction["recommendations"],
                predicted_ulcer_type=prediction["predicted_ulcer_type"],
                is_pud_positive=prediction["is_pud_positive"],
                prediction_details=prediction["prediction_details"],
                research_references=prediction["research_references"],
                drug_warnings=prediction["drug_warnings"],
            )
            messages.success(request, "Patient assessment saved and prediction generated.")
            return redirect(reverse("patients:report_detail", args=[assessment.id]))
    else:
        form = PatientAssessmentForm()

    return render(request, "patients/assessment.html", {"form": form, "prediction": prediction})


@verified_login_required
def symptom_log_create(request):
    latest_assessment = Assessment.objects.filter(patient__user=request.user).select_related("patient").first()
    if request.method == "POST":
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.estimated_risk = symptom_log_risk(form.cleaned_data, latest_assessment)
            log.save()
            messages.success(request, "Symptom log saved and risk trend updated.")
            return redirect("patients:dashboard")
    else:
        form = SymptomLogForm()
    return render(request, "patients/symptom_log.html", {"form": form, "latest_assessment": latest_assessment})


@verified_login_required
def chatbot(request):
    latest_assessment = Assessment.objects.filter(patient__user=request.user).select_related("patient").first()
    recent_logs = list(SymptomLog.objects.filter(user=request.user)[:5])
    response = None
    asked_message = ""
    if request.method == "POST":
        form = ChatbotForm(request.POST)
        if form.is_valid():
            asked_message = form.cleaned_data["message"]
            response = chatbot_guidance(
                asked_message,
                form.cleaned_data["severity_level"],
                latest_assessment,
                recent_logs,
            )
    else:
        form = ChatbotForm()
    return render(
        request,
        "patients/chatbot.html",
        {
            "form": form,
            "response": response,
            "asked_message": asked_message,
            "latest_assessment": latest_assessment,
            "recent_logs": recent_logs,
        },
    )


@verified_login_required
def patient_history(request):
    patients = Patient.objects.filter(user=request.user).prefetch_related("assessments")
    return render(request, "patients/history.html", {"patients": patients})


@verified_login_required
def delete_patient(request, patient_id):
    if request.method != "POST":
        return redirect("patients:history")
    patient = get_object_or_404(Patient, id=patient_id, user=request.user)
    patient_name = patient.full_name
    patient.delete()
    messages.success(request, f"{patient_name} record deleted successfully.")
    return redirect("patients:history")


@verified_login_required
def prediction_results(request):
    assessments = Assessment.objects.select_related("patient").filter(patient__user=request.user)
    return render(request, "patients/predictions.html", {"assessments": assessments})


@verified_login_required
def reports(request):
    assessments = Assessment.objects.select_related("patient").filter(patient__user=request.user)
    latest_assessment = assessments.first()
    chart_score = latest_assessment.risk_score if latest_assessment else 0
    chart_risk = latest_assessment.severity if latest_assessment else "No Data"
    chart_label = "Moderate" if chart_risk == "Medium" else chart_risk
    chart_confidence = min(chart_score + 4, 100) if latest_assessment else 0
    return render(
        request,
        "patients/reports.html",
        {
            "assessments": assessments,
            "latest_assessment": latest_assessment,
            "chart_score": chart_score,
            "chart_risk": chart_risk,
            "chart_label": chart_label,
            "chart_confidence": chart_confidence,
        },
    )


@verified_login_required
def report_detail(request, assessment_id):
    assessment = get_object_or_404(Assessment.objects.select_related("patient"), id=assessment_id, patient__user=request.user)
    return render(request, "patients/report_detail.html", {"assessment": assessment})


@verified_login_required
def export_report(request, assessment_id):
    assessment = get_object_or_404(Assessment.objects.select_related("patient"), id=assessment_id, patient__user=request.user)
    return render(request, "patients/export_report.html", {"assessment": assessment})


def architecture(request):
    return render(request, "patients/architecture.html")



@verified_login_required
def data_layer(request):
    if request.method == "POST":
        form = PUDDatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.original_filename = request.FILES["file"].name
            upload.save()
            process_pud_dataset_upload(upload)
            if upload.status == "processed":
                messages.success(request, "Dataset uploaded and processed")
            else:
                messages.error(request, upload.message)
            return redirect("patients:data_layer")
    else:
        form = PUDDatasetUploadForm()
    uploads = PUDDatasetUpload.objects.filter(user=request.user)[:8]
    latest = uploads[0] if uploads else None
    references = fetch_pubmed_references("peptic ulcer disease guideline H pylori NSAID", limit=4)
    return render(request, "patients/data_layer.html", {"form": form, "uploads": uploads, "latest": latest, "references": references})
