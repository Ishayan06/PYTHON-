import csv

students = [
    ["Roll No", "Name", "Marks"],
    [1, "Alice", 85],
    [2, "Bob", 90],
    [3, "Charlie", 78]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
