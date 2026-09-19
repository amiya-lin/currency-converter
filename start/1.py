class Student:
    def introduce(self):
        print("i'm student")


class Teacher:
    def introduce(self):
        print("i'm teacher")

student = Student()
teacher = Teacher()


people = [Student(),Teacher()]

for i in people:
    i.introduce()
