1. Single Inheritance
#Class Diagram: https://drive.google.com/file/d/14gZkhOaYrzg77rk_HfSKdCSjOyataRhS/view?usp=drivesdk

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
#Class Diagram: https://drive.google.com/file/d/1ylm6-5758zFhj0RAVNjg6I2THdgk5zZm/view?usp=drivesdk

class Family:
    def __init__(self, momname):
        self.momname = momname

class Parents(Family):
    def __init__(self, dadname, momname):
        self.dadname = dadname
        Family.__init__(self, momname)

class Daughter(Parents):
    def __init__(self, name, dadname, momname):
        self.name = name
        Parents.__init__(self, dadname, momname)

    def print_name(self):
        print(self.name)
        print("Mom name:", self.momname)
        print("Father name:", self.dadname)

obj = Daughter("Yeshua", "Joselito", "Eve")
obj.print_name()

3. Hierarchical Inheritance
#Class Diagram: https://drive.google.com/file/d/19_IHgPAaqjpGtWetqRZAwsgheI-3GvhT/view?usp=drivesdk

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

