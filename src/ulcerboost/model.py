def severity_from_score(score):
    if score >= 70:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"


def predict_ulcer_risk(features):
    """Simulated Gradient Boosting predictor for peptic ulcer risk.

    This keeps the same input/output shape expected from a real XGBoost model.
    Replace this function with a loaded model from `models/` when training is ready.
    """
    age = int(features.get("age") or 0)
    pain = int(features.get("pain_severity") or features.get("pain") or 0)
    score = 8
    score += 12 if age > 55 else 7 if age > 40 else 2
    score += pain * 6
    score += 18 if features.get("hpylori_status") == "positive" else 8 if features.get("hpylori_status") == "unknown" else 0
    score += 15 if features.get("nsaid_use") == "yes" else 8 if features.get("nsaid_use") == "sometimes" else 0
    score += 20 if features.get("bleeding_symptoms") == "yes" else 0
    score += 8 if features.get("smoking_history") == "yes" else 0
    score += 8 if features.get("alcohol_intake") == "high" else 4 if features.get("alcohol_intake") == "moderate" else 0
    score += 7 if features.get("stress_level") == "high" else 3 if features.get("stress_level") == "moderate" else 0
    risk_score = max(3, min(96, round(score)))
    severity = severity_from_score(risk_score)
    return {
        "risk_score": risk_score,
        "severity": severity,
        "recommendations": recommendations_for(severity, features),
    }


def recommendations_for(severity, features):
    if severity == "High":
        tips = [
            "Prioritize clinician review and screen for alarm symptoms.",
            "Confirm H. pylori status and document medication history.",
            "Generate a report for gastroenterology or senior clinical review.",
        ]
    elif severity == "Medium":
        tips = [
            "Schedule follow-up assessment and monitor symptom pattern.",
            "Review NSAID exposure, stress, diet, alcohol, and smoking factors.",
            "Consider H. pylori testing if status is unknown.",
        ]
    else:
        tips = [
            "Provide lifestyle guidance and symptom tracking.",
            "Escalate care if symptoms persist or alarm symptoms appear.",
            "Keep baseline history for future risk comparison.",
        ]
    if features.get("bleeding_symptoms") == "yes":
        tips.insert(0, "Bleeding symptoms require urgent medical evaluation.")
    return tips
