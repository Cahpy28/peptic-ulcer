from ulcerboost.model import predict_ulcer_risk


def test_high_risk_prediction():
    result = predict_ulcer_risk(
        {
            "age": 62,
            "pain_severity": 3,
            "hpylori_status": "positive",
            "nsaid_use": "yes",
            "bleeding_symptoms": "yes",
            "smoking_history": "yes",
            "alcohol_intake": "high",
            "stress_level": "high",
        }
    )
    assert result["severity"] == "High"
    assert result["risk_score"] >= 70
