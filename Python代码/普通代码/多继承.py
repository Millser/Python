#多继承例子
class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("我在游泳。。。。")

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("我在飞翔。。。。")

class Person():
    def __init__(self, name):
        self.name = name

    def worked(self):
        print("我在工作。。。")

class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name

class SwinMan(Person, Fish):
    def __init__(self, name):
        self.name = name

s = SuperMan('yueyue')
s.fly()
s.swim()

class Student(Person):
    def __init__(self, name):
        self.name = name