# Grade breakdown:
# 5 Assignments × 10% each = 50%
# Midterm 1 + Midterm 2 × 10% each = 20%
# Final Exam x 30%


# Content of index of the student list
# ID,First Name,Last Name,A1,A2,A3,A4,A5,M1,M2,Final Exam
student = [133727824,"Frodo","Baggins",94.1,94.7,52.9,98.3,91.1,69.4,97.3,57.2]
assgnGrades = student[3:8]
midTermGrades = student[8:10]
finalExamGrade = student[10:]

def aGrades(grades):
    agrades = 0
    for i in range(len(grades)):
        agrades = agrades + grades[i] * 0.1
        print(f"Assignment {i+1} Grade: {grades[i]:.2f}%")
    print(f"Assignment Grades: {agrades:.2f}%")
    return agrades

def mGrades(grades):
    mgradess = 0
    for i in range(len(grades)):
        mgradess = mgradess + grades[i] * 0.1
        print(f"Midterm {i+1} Grade: {grades[i]:.2f}%")
    print(f"Midterm Grades: {mgradess:.2f}%")
    return mgradess

def eGrades(grades):
    egrades = 0
    for i in range(len(grades)):
        egrades = egrades + grades[i] * 0.3
    print(f"Final Exam Grade: {egrades:.2f}%")
    return egrades

def main():
    totalGrade = aGrades(assgnGrades) + mGrades(midTermGrades) + eGrades(finalExamGrade)
    print(f"Total Grade: {totalGrade:.2f}%")
    return


main()