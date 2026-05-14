import re


PUD_SCOPE_WORDS = {
    "ulcer", "pud", "peptic", "gastric", "duodenal", "stomach", "abdomen", "abdominal",
    "epigastric", "burning", "pain", "h", "pylori", "hpylori", "helicobacter", "nsaid",
    "nsaids", "ibuprofen", "naproxen", "diclofenac", "aspirin", "bleeding", "melena",
    "black", "stool", "vomit", "blood", "acid", "ppi", "omeprazole", "pantoprazole",
    "food", "diet", "alcohol", "smoking", "stress", "symptom", "symptoms", "diagnosis",
    "treatment", "medication", "medicine", "antibiotic", "endoscopy", "complication",
    "warning", "urgent", "emergency", "care", "red", "flag", "danger",
}


APPROVED_PUD_KNOWLEDGE = [
    {
        "topic": "Typical peptic ulcer symptoms",
        "keywords": "symptoms epigastric burning gnawing upper abdominal pain nausea bloating belching fullness night meal food",
        "answer": (
            "Peptic ulcer disease commonly causes burning, gnawing, or aching pain in the upper abdomen. "
            "Some people also report nausea, bloating, belching, early fullness, reduced appetite, or pain that changes with meals or at night. "
            "Symptoms alone cannot prove that an ulcer is present or identify the exact ulcer type."
        ),
        "care": "Track pain timing, meal triggers, medicines used, vomiting, stool color, and symptom severity.",
        "urgent": "Seek urgent care if symptoms include vomiting blood, black/tarry stool, fainting, severe sudden pain, or persistent vomiting.",
        "reference": "NIDDK/Mayo Clinic: peptic ulcer symptoms and evaluation",
    },
    {
        "topic": "H. pylori and ulcer formation",
        "keywords": "h pylori hpylori helicobacter bacteria infection positive negative test breath stool antibiotic eradication",
        "answer": (
            "H. pylori is a common bacterial cause of gastric and duodenal ulcers. It can injure the stomach or duodenal lining and allow acid to cause ulceration. "
            "A positive H. pylori result usually needs clinician-directed eradication treatment, commonly antibiotics plus acid suppression, and confirmation that treatment worked."
        ),
        "care": "Ask about an approved H. pylori test if symptoms persist, recur, or if ulcer disease is suspected.",
        "urgent": "H. pylori itself is not usually an emergency, but bleeding, severe pain, or repeated vomiting is urgent.",
        "reference": "ACG/PubMed topics: H. pylori testing and eradication therapy",
    },
    {
        "topic": "NSAID and aspirin ulcer risk",
        "keywords": "nsaid nsaids ibuprofen naproxen diclofenac aspirin painkiller pain reliever steroid anticoagulant blood thinner ulcer bleeding",
        "answer": (
            "NSAIDs such as ibuprofen, naproxen, diclofenac, and aspirin can reduce protective stomach lining factors and increase ulcer or bleeding risk. "
            "Risk is higher with frequent use, older age, prior ulcer, H. pylori infection, steroids, anticoagulants, antiplatelet drugs, or heavy alcohol use."
        ),
        "care": "Do not self-treat ongoing ulcer pain with NSAIDs. Ask a clinician about safer pain options or gastroprotection.",
        "urgent": "Do not stop prescribed aspirin, anticoagulants, or heart medicines without medical advice, but seek urgent care for bleeding signs.",
        "reference": "FDA/OpenFDA drug-label topics: NSAID gastrointestinal ulceration and bleeding warnings",
    },
    {
        "topic": "Food and lifestyle guidance",
        "keywords": "food diet spicy caffeine coffee citrus tomato fried alcohol smoking meal late night lifestyle trigger avoid",
        "answer": (
            "Diet usually does not cause ulcers by itself, but some foods and habits can worsen symptoms. Common triggers include alcohol, smoking, coffee/caffeine, spicy meals, acidic foods, fried/fatty meals, and large late-night meals. "
            "Triggers differ by person, so the best approach is to record what repeatedly worsens symptoms."
        ),
        "care": "Use smaller meals, avoid personal triggers, limit alcohol, stop smoking if possible, and avoid lying down soon after heavy meals.",
        "urgent": "Lifestyle changes are not enough for alarm symptoms such as bleeding, severe pain, fainting, or weight loss.",
        "reference": "NIDDK/Mayo Clinic: symptom-trigger and lifestyle management",
    },
    {
        "topic": "Warning signs and urgent care",
        "keywords": "urgent warning emergency red flag black stool tarry melena blood vomit vomiting faint dizzy severe sudden pain weight loss anemia",
        "answer": (
            "Warning signs include vomiting blood, black or tarry stool, fainting, dizziness, severe sudden abdominal pain, persistent vomiting, unexplained weight loss, anemia symptoms, trouble swallowing, or rapidly worsening symptoms."
        ),
        "care": "These signs may suggest bleeding, obstruction, perforation, or another serious condition.",
        "urgent": "Seek urgent medical care immediately if any of these warning signs are present.",
        "reference": "Clinical safety references: gastrointestinal bleeding and peptic-ulcer complications",
    },
    {
        "topic": "Possible complications and effects",
        "keywords": "effects complications bleeding perforation obstruction anemia vomiting weight loss ulcer result outcome dangerous",
        "answer": (
            "Peptic ulcers can sometimes lead to bleeding, anemia, perforation, gastric outlet obstruction, persistent vomiting, reduced food intake, or weight loss. "
            "Most uncomplicated ulcers can improve with the right cause-directed treatment, but complications need prompt care."
        ),
        "care": "A risk score is only decision support; complications require clinical assessment, tests, and treatment planning.",
        "urgent": "Bleeding, severe sudden pain, repeated vomiting, or fainting should be treated as urgent.",
        "reference": "NIDDK/Mayo Clinic: peptic ulcer complications",
    },
    {
        "topic": "Gastric versus duodenal ulcer",
        "keywords": "gastric duodenal type kind ulcer type diagnosis positive negative stomach duodenum",
        "answer": (
            "Gastric ulcers occur in the stomach, while duodenal ulcers occur in the first part of the small intestine. "
            "Pain patterns may differ, but symptoms are not reliable enough to confirm the type. Endoscopy, H. pylori testing, medication history, and clinician review are used for confirmation."
        ),
        "care": "The system can estimate likely ulcer type from entered data, but it cannot replace diagnostic testing.",
        "urgent": "Any ulcer type with bleeding signs, severe pain, or persistent vomiting needs urgent review.",
        "reference": "PubMed clinical topics: gastric and duodenal ulcer diagnosis",
    },
    {
        "topic": "Low-risk or negative result meaning",
        "keywords": "negative low risk normal not positive no ulcer clear result unlikely",
        "answer": (
            "A low-risk or negative result means the entered information does not strongly match a peptic-ulcer pattern. "
            "It does not completely rule out ulcer disease or another digestive condition, especially if symptoms persist or worsen."
        ),
        "care": "Continue tracking symptoms and seek clinical review if pain is recurrent, persistent, or associated with alarm features.",
        "urgent": "A previous low-risk result should not delay urgent care for bleeding, fainting, severe sudden pain, or repeated vomiting.",
        "reference": "Clinical decision-support principle: low risk is not the same as no disease",
    },
    {
        "topic": "Medication safety",
        "keywords": "medication medicine drug ppi omeprazole pantoprazole lansoprazole h2 blocker famotidine antibiotic interaction allergy warning",
        "answer": (
            "Ulcer care may involve acid suppression such as PPIs or H2 blockers, H. pylori eradication antibiotics when indicated, and review of medicines that increase ulcer or bleeding risk. "
            "Medication choice depends on allergies, pregnancy status, kidney/liver disease, other prescriptions, and local clinical guidance."
        ),
        "care": "Use medicines exactly as prescribed and tell a clinician about NSAIDs, aspirin, steroids, blood thinners, supplements, and allergies.",
        "urgent": "Seek help for allergic reaction symptoms, bleeding, severe pain, or worsening symptoms while taking medicine.",
        "reference": "OpenFDA medication label topics and clinical prescribing safety",
    },
    {
        "topic": "What the AI can and cannot do",
        "keywords": "what is wrong diagnose diagnosis tell me positive accurate prediction result ai",
        "answer": (
            "The AI can explain peptic-ulcer risk factors and interpret stored risk information in plain language. "
            "It cannot diagnose you, confirm ulcer type, prescribe treatment, or replace endoscopy, H. pylori testing, laboratory tests, or clinician assessment."
        ),
        "care": "Use the answer as preparation for a healthcare discussion, especially if symptoms persist.",
        "urgent": "Do not use the AI for emergencies; seek urgent care for red-flag symptoms.",
        "reference": "Patient transparency principle: decision support is not a final diagnosis",
    },
]


def _tokens(text):
    return set(re.findall(r"[a-z0-9]+", str(text or "").lower()))


def _phrase_bonus(question, item):
    question = str(question or "").lower()
    bonus = 0
    for phrase in ("h. pylori", "h pylori", "black stool", "vomiting blood", "blood thinner", "urgent care", "side effect"):
        if phrase in question and phrase.replace(".", "") in (item["keywords"] + " " + item["answer"]).lower().replace(".", ""):
            bonus += 4
    return bonus


def retrieve_pud_knowledge(question, limit=3):
    query_tokens = _tokens(question)
    if not query_tokens:
        return []
    if not (query_tokens & PUD_SCOPE_WORDS):
        return []
    scored = []
    for item in APPROVED_PUD_KNOWLEDGE:
        topic_tokens = _tokens(item["topic"])
        keyword_tokens = _tokens(item["keywords"])
        answer_tokens = _tokens(item["answer"])
        score = (
            (len(query_tokens & topic_tokens) * 3)
            + (len(query_tokens & keyword_tokens) * 4)
            + len(query_tokens & answer_tokens)
            + _phrase_bonus(question, item)
        )
        if score:
            scored.append((score, item))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [item for _, item in scored[:limit]]


def _patient_context(latest_assessment, recent_logs):
    context = []
    if latest_assessment:
        context.append(
            f"Your latest stored assessment shows {latest_assessment.risk_score}% risk "
            f"({latest_assessment.severity}) with predicted category: {latest_assessment.predicted_ulcer_type}."
        )
        if latest_assessment.is_pud_positive:
            context.append("The stored assessment suggests PUD features are present, but confirmation still requires clinical evaluation.")
        else:
            context.append("The stored assessment does not strongly indicate PUD, but persistent or worsening symptoms should still be reviewed.")
    if recent_logs:
        avg_symptom = round(sum(log.severity_average for log in recent_logs) / len(recent_logs), 1)
        context.append(f"Your recent average symptom severity is {avg_symptom}/10.")
    return context


def advisor_answer_from_knowledge(question, severity_level, latest_assessment=None, recent_logs=None):
    recent_logs = recent_logs or []
    retrieved = retrieve_pud_knowledge(question)
    if not retrieved:
        return [
            "I can only answer questions related to peptic ulcer disease, H. pylori, NSAID risks, symptoms, medication safety, lifestyle triggers, warning signs, and your stored PUD risk profile.",
            "Please ask a peptic-ulcer-related question, for example: What warning signs need urgent care? or Are NSAIDs safe with ulcer symptoms?",
        ]

    answers = ["This is educational, non-diagnostic guidance. A qualified clinician must confirm diagnosis and treatment."]
    for item in retrieved:
        answers.append(f"{item['topic']}: {item['answer']}")
        answers.append(f"What to do: {item['care']}")
        if item["urgent"]:
            answers.append(f"Safety warning: {item['urgent']}")

    answers.extend(_patient_context(latest_assessment, recent_logs))
    if str(severity_level).lower() == "high":
        answers.append("Because you selected high symptom severity, prompt clinical review is recommended, especially if symptoms are new, worsening, or disrupting eating/sleep.")

    references = "; ".join(item["reference"] for item in retrieved)
    answers.append(f"Reference base: {references}.")
    return answers
