from .knowledge_base import advisor_answer_from_knowledge
from .model_training import predict_with_trained_model

def severity_from_score(score):
    if score >= 70:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"


def _yes(value):
    return str(value or "").lower() in {"yes", "positive", "frequent", "high", "true", "1"}


def _text_contains(data, *words):
    text = " ".join(str(data.get(key, "")) for key in ["symptoms", "diagnosis", "medications", "complications"]).lower()
    return any(word in text for word in words)


def infer_ulcer_type(data, risk_score):
    diagnosis = str(data.get("diagnosis", "")).lower()
    symptoms = str(data.get("symptoms", "")).lower()
    if "duoden" in diagnosis or "duoden" in symptoms or "night" in symptoms or "relieved by food" in symptoms:
        return "Duodenal Ulcer"
    if "gastric" in diagnosis or "stomach ulcer" in diagnosis or "worse after meal" in symptoms or "after eating" in symptoms:
        return "Gastric Ulcer"
    if risk_score < 25 and data.get("hpylori_status") == "negative" and data.get("nsaid_use") == "no":
        return "No active PUD indicated"
    if risk_score >= 40:
        return "Probable Peptic Ulcer Disease"
    return "PUD not strongly indicated"


def likely_causes(data):
    causes = []
    if data.get("hpylori_status") == "positive":
        causes.append("H. pylori infection is a major ulcer cause and should be clinically treated and confirmed eradicated.")
    elif data.get("hpylori_status") == "unknown":
        causes.append("Unknown H. pylori status remains an important unresolved cause; testing is recommended when symptoms persist.")
    if data.get("nsaid_use") in {"yes", "sometimes"} or _text_contains(data, "ibuprofen", "naproxen", "diclofenac", "aspirin"):
        causes.append("NSAID exposure may weaken stomach lining protection and increase ulcer or bleeding risk.")
    if data.get("smoking_history") == "yes":
        causes.append("Smoking may slow ulcer healing and increase recurrence risk.")
    if data.get("alcohol_intake") in {"moderate", "high"}:
        causes.append("Alcohol can irritate the gastric lining and worsen acid-related symptoms.")
    if data.get("stress_level") == "high":
        causes.append("High stress may worsen pain perception, sleep, eating patterns, and symptom flares.")
    if data.get("previous_ulcer") == "yes":
        causes.append("Previous ulcer history increases recurrence risk and should influence follow-up planning.")
    if not causes:
        causes.append("No dominant ulcer cause was identified from the entered data; consider clinical review if symptoms persist.")
    return causes


def symptom_effect_summary(data, ulcer_type, risk_score):
    symptoms = []
    effects = []
    if _yes(data.get("epigastric_pain")) or _text_contains(data, "epigastric", "burning", "upper abdominal"):
        symptoms.append("epigastric or burning upper-abdominal pain")
    if _yes(data.get("bloating")) or _text_contains(data, "bloating", "belching", "fullness"):
        symptoms.append("bloating/fullness")
    if _yes(data.get("bleeding_symptoms")) or _text_contains(data, "blood", "black stool", "melena", "vomit blood"):
        symptoms.append("possible bleeding symptoms")
        effects.append("possible gastrointestinal bleeding, which requires urgent medical assessment")
    if _yes(data.get("weight_loss")) or _text_contains(data, "weight loss"):
        symptoms.append("unexplained weight loss")
        effects.append("nutritional decline or alarm-feature concern")
    if data.get("complications"):
        effects.append(f"reported complications: {data.get('complications')}")
    if not symptoms:
        symptoms.append("no specific ulcer symptom pattern clearly entered")
    if risk_score >= 70:
        effects.append("higher probability of clinically significant PUD requiring prompt review")
    elif risk_score >= 40:
        effects.append("moderate likelihood of PUD or acid-related disease requiring follow-up")
    else:
        effects.append("low PUD likelihood from entered features, but persistent symptoms still need review")
    return {"symptoms": symptoms, "effects": effects, "ulcer_type_reasoning": ulcer_type}


def recommendations_for(severity, data):
    items = []
    if severity == "High":
        items.extend([
            "Arrange prompt clinical review, especially if pain is persistent, severe, recurrent, or associated with vomiting or bleeding signs.",
            "Assess for alarm symptoms: black stool, vomiting blood, anemia, unexplained weight loss, progressive swallowing difficulty, fainting, or severe sudden pain.",
            "Confirm H. pylori status and document eradication plan if positive.",
            "Review NSAID, aspirin, steroid, anticoagulant, and pain-reliever exposure with a clinician.",
        ])
    elif severity == "Medium":
        items.extend([
            "Schedule follow-up assessment and monitor pain timing, food triggers, medication exposure, and symptom trend.",
            "Request H. pylori testing if status is unknown or symptoms persist.",
            "Reduce avoidable NSAID use and discuss gastroprotection or safer alternatives with a clinician.",
        ])
    else:
        items.extend([
            "Continue symptom tracking and lifestyle modification while watching for alarm symptoms.",
            "Seek clinical review if symptoms persist, recur, or worsen despite conservative management.",
            "Maintain a record of meals, medicines, pain timing, stool changes, and stress patterns.",
        ])
    if data.get("hpylori_status") == "positive":
        items.append("Discuss guideline-based H. pylori eradication therapy and post-treatment confirmation testing.")
    if data.get("nsaid_use") == "yes":
        items.append("Frequent NSAID use is a modifiable risk factor; avoid self-treatment and ask about safer pain-control options.")
    if data.get("bleeding_symptoms") == "yes":
        items.insert(0, "Bleeding symptoms require urgent medical evaluation.")
    items.append("This prediction supports clinical decision-making and is not a standalone diagnosis.")
    return items


def simulated_xgboost_prediction(data, dataset_profile=None, research_references=None, drug_warnings=None):
    age = int(data.get("age") or 0)
    pain = int(data.get("pain_severity") or 0)
    contributions = {
        "Age": 12 if age > 55 else 7 if age > 40 else 2,
        "Pain Severity": pain * 7,
        "H. pylori Status": 22 if data.get("hpylori_status") == "positive" else 10 if data.get("hpylori_status") == "unknown" else -8,
        "NSAID Usage": 18 if data.get("nsaid_use") == "yes" else 9 if data.get("nsaid_use") == "sometimes" else 0,
        "Bleeding Symptoms": 24 if data.get("bleeding_symptoms") == "yes" else 0,
        "Smoking History": 8 if data.get("smoking_history") == "yes" else 0,
        "Alcohol Intake": 8 if data.get("alcohol_intake") == "high" else 4 if data.get("alcohol_intake") == "moderate" else 0,
        "Stress Level": 7 if data.get("stress_level") == "high" else 3 if data.get("stress_level") == "moderate" else 0,
        "Diet Pattern": 7 if data.get("diet_pattern") == "high" else 3 if data.get("diet_pattern") == "moderate" else 0,
        "Previous Ulcer": 12 if data.get("previous_ulcer") == "yes" else 0,
        "Complications": 14 if data.get("complications") else 0,
        "Medication Risk": 12 if _text_contains(data, "ibuprofen", "naproxen", "diclofenac", "aspirin") else 0,
    }
    calibration = (dataset_profile or {}).get("calibration", {}) if isinstance(dataset_profile, dict) else {}
    if calibration:
        if calibration.get("hpylori_status", 0) >= 50 and data.get("hpylori_status") == "positive":
            contributions["Dataset H. pylori Pattern"] = 8
        if calibration.get("nsaid_use", 0) >= 50 and data.get("nsaid_use") in {"yes", "sometimes"}:
            contributions["Dataset NSAID Pattern"] = 8

    raw_score = 10 + sum(contributions.values())
    risk_score = max(3, min(97, round(raw_score)))
    severity = severity_from_score(risk_score)
    ulcer_type = infer_ulcer_type(data, risk_score)
    is_positive = risk_score >= 40 and ulcer_type not in {"No active PUD indicated", "PUD not strongly indicated"}
    total = max(sum(value for value in contributions.values() if value > 0), 1)
    feature_importance = {
        key: round((value / total) * 100)
        for key, value in sorted(contributions.items(), key=lambda item: item[1], reverse=True)
        if value > 0
    }
    details = {
        "likely_causes": likely_causes(data),
        "symptom_effect_summary": symptom_effect_summary(data, ulcer_type, risk_score),
        "positivity_interpretation": "PUD features are present" if is_positive else "PUD is not strongly indicated from entered data",
        "clinical_guidelines": recommendations_for(severity, data),
        "model_note": "Risk estimate uses validated fields and can be calibrated by uploaded CSV dataset profiles. Final diagnosis requires clinician review/testing.",
    }
    trained_prediction = predict_with_trained_model(data)
    if trained_prediction:
        risk_score = trained_prediction["risk_score"]
        severity = severity_from_score(risk_score)
        ulcer_type = infer_ulcer_type(data, risk_score)
        is_positive = trained_prediction["is_pud_positive"] and ulcer_type not in {"No active PUD indicated", "PUD not strongly indicated"}
        details["symptom_effect_summary"] = symptom_effect_summary(data, ulcer_type, risk_score)
        details["positivity_interpretation"] = "PUD features are present" if is_positive else "PUD is not strongly indicated from entered data"
        details["clinical_guidelines"] = recommendations_for(severity, data)
        details["model_note"] = (
            "Risk estimate was generated by the trained XGBoost pipeline saved in the models folder. "
            "Final diagnosis still requires clinician review/testing."
        )
    return {
        "risk_score": risk_score,
        "severity": severity,
        "feature_importance": feature_importance,
        "recommendations": details["clinical_guidelines"],
        "predicted_ulcer_type": ulcer_type,
        "is_pud_positive": is_positive,
        "prediction_details": details,
        "research_references": research_references or [],
        "drug_warnings": drug_warnings or [],
    }


def symptom_log_risk(data, latest_assessment=None):
    pain = int(data.get("abdominal_pain") or 0)
    nausea = int(data.get("nausea") or 0)
    heartburn = int(data.get("heartburn") or 0)
    appetite_loss = int(data.get("appetite_loss") or 0)
    baseline = latest_assessment.risk_score * 0.35 if latest_assessment else 12
    symptom_score = (pain * 4) + (nausea * 2.5) + (heartburn * 2.5) + (appetite_loss * 2)
    return max(3, min(96, round(baseline + symptom_score)))


def chatbot_guidance(message, severity_level, latest_assessment=None, recent_logs=None):
    return advisor_answer_from_knowledge(message, severity_level, latest_assessment, recent_logs)
