from array import array

students = ["Ram", "Prateek", "Shahraan", "Aryan", "Ayaan", "Ekansh"]

subjects = ("Maths", "Science", "English")

grades = {
    "Ram": [85, 90, 78],
    "Ayaan": [92, 88, 95],
    "Shahraan": [75, 80, 72],
    "Aryan": [89, 94, 91],
    "Ekansh":[30, 84, 93],
    "Prateek":[66, 53, 99]
}
print(grades)
student_set = set(students)

marks_array = array('i', grades["Aryan"])

print("===== GRADE BOOK =====")


while True:
    print("\n1. Show all students")
    print("2. Show a student's grades")
    print("3. Calculate average")
    print("4. Add a student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nStudents:")
        for student in student_set:
            print(student)

    elif choice == "2":
        name = input("Enter student name: ")

        if name in grades:
            
            for subject, mark in zip(subjects, grades[name]):
                print(subject, ":", mark)
        else:
            print("Student not found!")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in grades:
            marks = list(map(int, grades[name]))

            average = sum(marks) / len(marks)

            print("Average:", average)

            if average >= 90:
                print("Grade: A")
            elif average >= 80:
                print("Grade: B")
            elif average >= 70:
                print("Grade: C")
            else:
                print("Grade: D")
        else:
            print("Student not found!")


    elif choice == "4":
        name = input("Enter new student name: ").capitalize

        if name in grades:
            print("Student already exists!")
        else:
            marks = []

            for subject in subjects:
                mark = int(input("Enter marks for " + subject + ": "))
                marks.append(mark)

            grades[name] = marks
            students.append(name)
            student_set.add(name)

            print("Student added successfully!")

    elif choice == "5":
        print("Thank you for using the Grade Book!")
        exit()

    else:
        print("Invalid choice. Try again.")
