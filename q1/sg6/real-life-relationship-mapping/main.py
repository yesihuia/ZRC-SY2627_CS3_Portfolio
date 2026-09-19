class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Yeshua", "033")
student2 = Student("Matthew", "079")

course = Course("Computer Science")

course.add_student(student1)
course.add_student(student2)

print(course.name)

for student in course.students:
    print(student.name)