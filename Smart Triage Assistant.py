from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

# Labels in English and Greek
labels = {
    "name": {"en": "Name", "el": "Όνομα"},
    "gender": {"en": "Gender", "el": "Φύλο"},
    "male": {"en": "Male", "el": "Άρρεν"},  # corrected spelling
    "female": {"en": "Female", "el": "Γυναίκα"},
    "insurance": {"en": "Insurance Number", "el": "Αριθμός Ασφάλισης"},
    "symptoms": {"en": "Symptoms", "el": "Συμπτώματα"},
    "submit": {"en": "Submit", "el": "Υποβολή"},
    "language": {"en": "Language", "el": "Γλώσσα"},
    "result": {"en": "Emergency Result", "el": "ΕΠΙΠΕΔΟ ΕΠΕΙΓΟΥΣΑΣ ΑΝΑΓΚΗΣ"},
    "next_step": {"en": "Next Step", "el": "Επόμενο Βήμα"},
    "date": {"en": "Date", "el": "Ημερομηνία"}
}

symptom_map = {
    "cardiology": ["chest_pain", "palpitations", "dizziness"],
    "pulmonology": ["cough", "shortness_breath", "wheezing"],
    "neurology": ["headache", "numbness", "seizure"],
    "gastroenterology": ["nausea", "abdominal_pain", "diarrhea"],
    "general": ["fever", "fatigue", "back_pain"]
}

symptom_labels = {
    "chest_pain": {"en": "Chest Pain", "el": "Πόνος στο στήθος"},
    "palpitations": {"en": "Palpitations", "el": "Αρρυθμίες"},
    "dizziness": {"en": "Dizziness", "el": "Ζάλη"},
    "cough": {"en": "Cough", "el": "Βήχας"},
    "shortness_breath": {"en": "Shortness of Breath", "el": "Δύσπνοια"},
    "wheezing": {"en": "Wheezing", "el": "Συριγμός"},
    "headache": {"en": "Headache", "el": "Πονοκέφαλος"},
    "numbness": {"en": "Numbness", "el": "Μούδιασμα"},
    "seizure": {"en": "Seizure", "el": "Επιληψία"},
    "nausea": {"en": "Nausea", "el": "Ναυτία"},
    "abdominal_pain": {"en": "Abdominal Pain", "el": "Κοιλιακός Πόνος"},
    "diarrhea": {"en": "Diarrhea", "el": "Διάρροια"},
    "fever": {"en": "Fever", "el": "Πυρετός"},
    "fatigue": {"en": "Fatigue", "el": "Κόπωση"},
    "back_pain": {"en": "Back Pain", "el": "Πόνος στην Πλάτη"}
}

symptom_severity = {
    "chest_pain": "high",
    "seizure": "high",
    "shortness_breath": "high",
    "dizziness": "medium",
    "palpitations": "medium",
    "abdominal_pain": "medium",
    "fever": "medium",
    "cough": "low",
    "headache": "low",
    "numbness": "low",
    "fatigue": "low",
    "wheezing": "low",
    "nausea": "low",
    "diarrhea": "low",
    "back_pain": "low"
}

@app.route("/", methods=["GET", "POST"])
def index():
    name = gender = insurance = result = department = department_label = ""
    selected = []
    lang = request.args.get("lang", "en")
    date_value = ""

    if request.method == "POST":
        name = request.form.get("name", "")
        gender = request.form.get("gender", "")
        insurance = request.form.get("insurance", "")
        selected = request.form.getlist("symptoms")
        date_value = request.form.get("date", "")
        # Determine emergency level based on symptom severity
        if any(symptom_severity.get(s) == "high" for s in selected):
            result = {"en": "High", "el": "Υψηλό"}[lang]
        elif any(symptom_severity.get(s) == "medium" for s in selected):
            result = {"en": "Medium", "el": "Μέτριο"}[lang]
        else:
            result = {"en": "Low", "el": "Χαμηλό"}[lang]

        # Determine department
        dept_scores = {dept: 0 for dept in symptom_map}
        for symptom in selected:
            for dept, symptoms in symptom_map.items():
                if symptom in symptoms:
                    dept_scores[dept] += 1

        department = max(dept_scores, key=dept_scores.get) if selected else ""
        if department:
            department_label = department.capitalize() if lang == "en" else {
                "cardiology": "Καρδιολογία",
                "pulmonology": "Πνευμονολογία",
                "neurology": "Νευρολογία",
                "gastroenterology": "Γαστρεντερολογία",
                "general": "Γενική Ιατρική"
            }[department]
    else:
        date_value = date.today().isoformat()

    return render_template("index.html", labels=labels, symptoms=symptom_labels, lang=lang, name=name,
                           gender=gender, insurance=insurance, selected=selected,
                           result=result, department=department_label, date_value=date_value)

if __name__ == "__main__":
    app.run(debug=True)




