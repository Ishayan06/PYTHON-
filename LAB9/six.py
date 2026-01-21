class Person:
    def show(self):
        print("Person class")

class Student(Person):
    def show_student(self):
        print("Student class")

class GraduateStudent(Student):
    def show_graduate(self):
        print("Graduate Student class")

g = GraduateStudent()
g.show()
g.show_student()
g.show_graduate()
