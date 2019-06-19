class Dog:
    name = "Animal"
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    
    def bark(self):
        print("Woof!")
    

    def eat(self):
        print("Doggo is eating")

    
    def show_name(self):
        print(self.name)

class Cat(Dog):
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
    

    def eat(self):
        print("Catto is eating")

    def bark(self):
        print("Meow!")
    

    def show_name(self):
        print(self.name)
    
    

ajit = Dog("Waghmode", "kalu", "17")
pratik = Cat("Kapadnis", "undir", "17")

ajit.bark()
pratik.bark()
ajit.eat()
pratik.eat()
ajit.show_name()
pratik.show_name()