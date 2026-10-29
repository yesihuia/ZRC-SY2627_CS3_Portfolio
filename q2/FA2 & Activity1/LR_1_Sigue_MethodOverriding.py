class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name, "makes a sound.")

    def eat(self):
        print(self.name, "is eating.")

class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly.")

    def eat(self):
        print(self.name, "eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets.")

    def eat(self):
        print(self.name, "eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters.")

    def eat(self):
        print(self.name, "eats bananas.")

lion = Lion("Barry")
elephant = Elephant("Gatty")
monkey = Monkey("Georgie")

animals = [lion, elephant, monkey]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
