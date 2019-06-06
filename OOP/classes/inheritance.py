class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print("Animal Created")

    def eat(self):
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")


class Dog(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        print("Dog created!")

    def who_am_i(self):
        print("I am a cute doggo")


def print_animal(animal):
    print(f"Name is {animal.name}")
    print(f"Age is {animal.age}")


ani = Dog("ani", 4)
print(ani.age)
print(ani.name)
ani.eat()
ani.who_am_i()
print_animal(ani)
