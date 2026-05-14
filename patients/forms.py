from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Assessment, Patient, PUDDatasetUpload, SymptomLog


class VerifiedAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                inactive_user = User.objects.filter(username__iexact=username, is_active=False).first()
                if inactive_user and inactive_user.check_password(password):
                    raise forms.ValidationError(
                        "Please verify your email before signing in. You can resend the verification link below.",
                        code="inactive",
                    )
                raise self.get_invalid_login_error()
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    consent = forms.BooleanField(
        required=True,
        label="I understand my patient rights and consent to secure processing of my PUD assessment data.",
        help_text="You can access your records, review generated reports, and request deletion of your saved patient history from the dashboard.",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "consent")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1", "")
        checks = [
            (len(password) >= 12, "at least 12 characters"),
            (any(char.isupper() for char in password), "one uppercase letter"),
            (any(char.islower() for char in password), "one lowercase letter"),
            (any(char.isdigit() for char in password), "one number"),
            (any(not char.isalnum() for char in password), "one symbol"),
        ]
        missing = [label for passed, label in checks if not passed]
        if missing:
            raise forms.ValidationError("Use a very strong password with " + ", ".join(missing) + ".")
        return password

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "Choose a username",
            "email": "you@example.com",
            "password1": "Create a strong password",
            "password2": "Confirm password",
        }
        for name, field in self.fields.items():
            if name != "consent":
                field.widget.attrs.setdefault("class", "input-control")
                field.widget.attrs.setdefault("placeholder", placeholders.get(name, ""))
                if name in {"password1", "password2"}:
                    field.widget.attrs.setdefault("data-password-input", "true")


class EmailCodeVerificationForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={"class": "input-control", "placeholder": "you@example.com", "autocomplete": "email"}),
    )
    code = forms.CharField(
        label="Verification Code",
        min_length=6,
        max_length=6,
        widget=forms.TextInput(
            attrs={
                "class": "input-control verification-code-input",
                "placeholder": "Enter 6-digit code",
                "autocomplete": "one-time-code",
                "inputmode": "numeric",
            }
        ),
    )

    def clean_code(self):
        code = self.cleaned_data["code"].strip()
        if not code.isdigit():
            raise forms.ValidationError("Enter the 6-digit code sent to your email.")
        return code


class PatientAssessmentForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="Patient Name")
    age = forms.IntegerField(min_value=1, max_value=120)
    gender = forms.ChoiceField(choices=[("", "Select gender"), *Patient.GENDER_CHOICES])
    phone = forms.CharField(max_length=32, required=False)
    systolic_bp = forms.IntegerField(min_value=60, max_value=240, required=False, label="Systolic BP (mmHg)")
    diastolic_bp = forms.IntegerField(min_value=40, max_value=160, required=False, label="Diastolic BP (mmHg)")
    weight = forms.DecimalField(min_value=20, max_value=250, required=False, label="Weight (kg)")
    pain_severity = forms.ChoiceField(choices=Assessment.PAIN_CHOICES)
    hpylori_status = forms.ChoiceField(choices=Assessment.HPYLORI_CHOICES, label="H. pylori Status")
    nsaid_use = forms.ChoiceField(choices=Assessment.NSAID_CHOICES, label="NSAID Use")
    bleeding_symptoms = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    smoking_history = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    alcohol_intake = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    stress_level = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    diet_pattern = forms.ChoiceField(choices=Assessment.LEVEL_CHOICES)
    previous_ulcer = forms.ChoiceField(choices=Assessment.YES_NO_CHOICES)
    diagnosis = forms.CharField(max_length=160, required=False, label="Previous/Current Diagnosis", widget=forms.TextInput(attrs={"placeholder": "e.g. suspected gastritis, PUD, none"}))
    medications = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 3, "placeholder": "e.g. ibuprofen, aspirin, omeprazole, antibiotics"}))
    complications = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 3, "placeholder": "e.g. bleeding, anemia, perforation, obstruction, none"}))
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False,
        help_text="Clinical notes, presenting symptoms, medication history, and relevant observations.",
    )

    def clean_pain_severity(self):
        return int(self.cleaned_data["pain_severity"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Enter full name",
            "age": "e.g. 42",
            "phone": "Optional phone number",
            "systolic_bp": "e.g. 120",
            "diastolic_bp": "e.g. 80",
            "weight": "e.g. 70",
            "symptoms": "Burning pain, nausea, meal triggers, medication history",
            "diagnosis": "e.g. suspected gastritis, PUD, none",
            "medications": "List current medicines and pain relievers",
            "complications": "Bleeding, anemia, obstruction, perforation, none",
        }
        for name, field in self.fields.items():
            field.widget.attrs.setdefault("class", "input-control")
            if name in placeholders:
                field.widget.attrs.setdefault("placeholder", placeholders[name])


class SymptomLogForm(forms.ModelForm):
    class Meta:
        model = SymptomLog
        fields = [
            "abdominal_pain",
            "nausea",
            "heartburn",
            "appetite_loss",
            "medication_taken",
            "meal_trigger",
            "notes",
        ]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input-control")


class ChatbotForm(forms.Form):
    severity_level = forms.ChoiceField(
        choices=[("low", "Low"), ("moderate", "Moderate"), ("high", "High")],
        label="Current Symptom Severity",
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Ask a peptic ulcer question, for example: What warning signs need urgent care?"}),
        label="Message",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "input-control")





class PUDDatasetUploadForm(forms.ModelForm):
    class Meta:
        model = PUDDatasetUpload
        fields = ["file"]
        widgets = {
            "file": forms.ClearableFileInput(attrs={"class": "input-control", "accept": ".csv"}),
        }
        labels = {"file": "Upload real PUD CSV dataset"}
        help_texts = {"file": "CSV fields should include age, symptoms, NSAID use, H. pylori status, smoking/alcohol, diagnosis, medications, and complications."}

    def clean_file(self):
        file = self.cleaned_data["file"]
        if not file.name.lower().endswith(".csv"):
            raise forms.ValidationError("Upload a CSV dataset file.")
        return file
