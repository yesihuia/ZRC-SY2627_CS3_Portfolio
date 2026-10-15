1. Single Inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def func1(self):
        print("Parent's name:", self.name)


class Child(Parent):
    def func2(self):
        print(self.name, "is a child.")


obj1 = Child("Sophia")
obj1.func1()
obj1.func2()

obj1.set_name("Alex")
print("Updated name:", obj1.get_name())

obj2 = Child("Sam")
obj2.func1()
obj2.func2()

2. Multilevel Inheritance


class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, name):
        self.grandfathername = name


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print("Grandfather:", self.grandfathername)
        print("Father:", self.fathername)
        print("Son:", self.sonname)


s1 = Son("Prince", "Rampal", "Lal mani")
s1.print_name()

s1.set_sonname("Alex")
s1.set_fathername("John")
s1.set_grandfathername("Robert")

print("Updated names:")
s1.print_name()

s2 = Son("Sam", "David", "Michael")
print("Second family:")
s2.print_name()

3. Hierarchical Inheritance


class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def func1(self):
        print("Name:", self.name)


class Child1(Parent):
    def func2(self):
        print(self.name, "belongs to Child1.")


class Child2(Parent):
    def func3(self):
        print(self.name, "belongs to Child2.")


object1 = Child1("Sophia")
object2 = Child2("Alex")

object1.func1()
object1.func2()

object2.func1()
object2.func3()

object1.set_name("Sam")
print("Updated Child1 name:", object1.get_name())

object3 = Child2("Jamie")
object3.func1()
object3.func3()
