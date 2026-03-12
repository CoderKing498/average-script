name = input("Enter student's name: ")

grades = {}

try:
    grades["Activity"] = float(input("Enter the activity grade: "))
    grades["Homework"] = float(input("Enter the homework grade: "))
    grades["Exam"] = float(input("Enter the exam grade: "))

    average = sum(grades.values()) / len(grades)

    print("\nStudent:", name)
    print("\nGrades:")

    for category, grade in grades.items():
        print(category + ":", grade)

    print("\nAverage grade:", round(average, 2))

    if average >= 3.0:
        print("Status: Passed")
    else:
        print("Status: Failed")

except ValueError:
    print("Error: Please enter valid numeric grades.")


