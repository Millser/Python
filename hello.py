class Student():
    pass

mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业")

        return None

yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.name)

yueyue.doHomework()