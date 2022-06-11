student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


#
higest_score = 0
for score in student_scores:
    if score > higest_score:
        higest_score = score

print(f"The hihest score is : {higest_score}")
