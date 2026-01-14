with open("students.txt", "w") as f:
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")
        f.write(f"Name: {name}, Roll: {roll}, Marks: {marks}\n")

print("Student details saved successfully.")
