# Training Data Folder

Place approved, labeled dataset exports here before training.

Recommended sources:

- MIMIC-IV hospital diagnosis data
- MIMIC-IV-ED emergency diagnosis and medication data
- eICU Collaborative Research Database
- NHANES risk-factor tables for enrichment only

Your final training CSV should include:

```csv
age,gender,symptoms,nsaid_use,hpylori_status,smoking,alcohol,diagnosis,diagnosis_code,ulcer_type,pud_positive,medications,complications
```

Do not include patient names, phone numbers, addresses, or direct identifiers.
