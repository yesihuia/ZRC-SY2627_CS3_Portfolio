class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

    def make_sound(self):
        print(self.name, "makes a sound.")

class Lion(Animal):
    def eat(self):
        print(self.name, "eats fresh meat.")

    def make_sound(self):
        print(self.name, "roars loudly.")

class Elephant(Animal):
    def eat(self):
        print(self.name, "eats grass and fruits.")

    def make_sound(self):
        print(self.name, "trumpets.")

class Monkey(Animal):
    def eat(self):
        print(self.name, "eats bananas.")

    def make_sound(self):
        print(self.name, "chatters.")

lion = Lion("Leo")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals:
    animal.eat()
    animal.make_sound()
    print()
