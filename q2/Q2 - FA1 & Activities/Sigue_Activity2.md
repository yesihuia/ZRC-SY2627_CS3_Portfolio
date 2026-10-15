1. Single Inheritance

class Parent:
    def func1(self):
        print("This is Yeshua's family.")

class Child(Parent):
    def func2(self):
        print("My name is Yeshua.")

obj = Child()
obj.func1()
obj.func2()

2. Multilevel Inheritance

class Grandfather:
    def __init__(self, name):
        self.name = name

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather:", self.name)
        print("Father:", self.fathername)
        print("Son:", self.sonname)

obj = Son("Yeshua", "Joselito", "Grandfather")
obj.print_name()


3. Hierarchical Inheritance

class Parent:
    def func1(self):
        print("My name is Yeshua.")

class Child1(Parent):
    def func2(self):
        print("My mom is Eve.")

class Child2(Parent):
    def func3(self):
        print("My dad is Joselito.")
        print("My sister is Uzziah.")

obj1 = Child1()
obj1.func1()
obj1.func2()

obj2 = Child2()
obj2.func1()
obj2.func3()

