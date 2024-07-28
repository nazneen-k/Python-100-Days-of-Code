students_score={
    "Tom":99,
    "Hermione":98,
    "Draco":74,
    "Neville":62
}

students_grade={}

for student in students_score:
    score=students_score[student]
    if score > 00:
        students_grade[student]="Outstanding"
    elif score > 80:
        students_grade[student]="Exceed Expectations"
    elif score > 70:
        students_grade[student]="Acceptable"
    else:
        students_grade[student]="Fail"

print(students_grade)