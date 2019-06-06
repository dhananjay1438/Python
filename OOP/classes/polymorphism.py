class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def speak(self):
        print("woof!")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("meow!")


alex = Dog("alex", 1)
franchis = Cat("franchis", 3)

alex.speak()
franchis.speak()
