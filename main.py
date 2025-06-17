import openai
import os

openai.api_key = "xxx"

correct_answers = {
    "implicit_meaning": "Α",
    "ambiguity": ["Β", "Β", "Γ"],
    "recycling_ad": "Α",
    "car_ad": "Α"
}

students_answers = [
    {
        "name": "Μαρία Παπαδοπούλου",
        "implicit_meaning": "Α",
        "ambiguity": ["Β", "Β", "Γ"],
        "recycling_ad": "Α",
        "car_ad": "Α"
    },
    {
        "name": "Γιάννης Αντωνίου",
        "implicit_meaning": "Γ",
        "ambiguity": ["Α", "Β", "Γ"],
        "recycling_ad": "Β",
        "car_ad": "Β"
    }
]

def generate_comment(student):
    score = 0
    comment_parts = []

    if student["implicit_meaning"] == correct_answers["implicit_meaning"]:
        score += 1
        comment_parts.append("Καλή κατανόηση της μη ρητής επικοινωνίας.")
    else:
        comment_parts.append("Χρειάζεται βελτίωση στην κατανόηση υπονοούμενων νοημάτων.")

    ambiguity_score = sum([1 for a, b in zip(student["ambiguity"], correct_answers["ambiguity"]) if a == b])
    score += ambiguity_score
    if ambiguity_score == 3:
        comment_parts.append("Εξαιρετική κατανόηση της αμφισημίας.")
    elif ambiguity_score == 2:
        comment_parts.append("Καλή προσπάθεια στην αμφισημία, με μικρά λάθη.")
    else:
        comment_parts.append("Ασάφεια στην κατανόηση της αμφισημίας.")

    if student["recycling_ad"] == correct_answers["recycling_ad"]:
        score += 1
        comment_parts.append("Κατανόηση της επιρροής της περιβαλλοντικής διαφήμισης.")
    else:
        comment_parts.append("Χρειάζεται προσοχή στην αξιολόγηση διαφημιστικών σκοπών.")

    if student["car_ad"] == correct_answers["car_ad"]:
        score += 1
        comment_parts.append("Ορθή αξιολόγηση των πειστικών τεχνικών στη διαφήμιση αυτοκινήτου.")
    else:
        comment_parts.append("Η διαφήμιση αυτοκινήτου παραπλάνησε· προσοχή στα λανθάνοντα μηνύματα.")

    total_score = f"Συνολική βαθμολογία: {score}/6"
    comment = " ".join(comment_parts)

    print(f"Μαθητής: {student['name']}")
    print(total_score)
    print("Σχόλιο:", comment)
    print("-" * 40)

    return score, comment

def generate_custom_questions(student_name, weaknesses):
    prompt = f"""Είσαι εκπαιδευτικός βοηθός. Δημιούργησε 3 προσαρμοσμένες ερωτήσεις γλωσσικής επίγνωσης για μαθητή με αδυναμίες: {weaknesses}. 
Κράτα τις ερωτήσεις σχετικές με μη ρητή επικοινωνία, αμφισημία και διαφημίσεις."""
    prompt = prompt.encode('utf-8').decode('utf-8')

    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Είσαι βοηθός δημιουργίας εκπαιδευτικού υλικού."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7,
    )
    questions = response.choices[0].message.content.strip()
    return questions

def sanitize_filename(name):
    # Μετατρέπει το όνομα σε μικρά και χωρίς κενά, για όνομα αρχείου
    return name.lower().replace(" ", "_").replace("ά", "α").replace("έ", "ε").replace("ή", "η").replace("ί", "ι").replace("ό", "ο").replace("ύ", "υ").replace("ώ", "ω")

for student in students_answers:
    score, comment = generate_comment(student)

    weaknesses = []
    if "βελτίωση" in comment or "Ασάφεια" in comment or "Χρειάζεται" in comment:
        weaknesses.append("Ενίσχυση κατανόησης μη ρητής επικοινωνίας και αμφισημίας")
    
    if weaknesses:
        questions = generate_custom_questions(student["name"], ", ".join(weaknesses))
        filename = sanitize_filename(student["name"]) + "_questions.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Προσαρμοσμένες ερωτήσεις για {student['name']}:\n\n")
            f.write(questions)
        print(f"Οι ερωτήσεις αποθηκεύτηκαν στο αρχείο: {filename}")