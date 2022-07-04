#  student scores and grade
student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# grade
student_grades = {}

for name, score in student_score.items():
    if score > 90:
        student_grades[name] = "Outstanding"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Failed"

print(student_grades)
