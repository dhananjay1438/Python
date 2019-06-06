class FirstClass:
    def __init__(self, param):
        self.param = param
        print(param)


class Dog:
    dog_age = 0

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def check_if_dog_is_old_by_class_variables(self):
        """
        DOCSTRING:
        Checks if dog is old or not
        :param self:
        """
        if self.dog_age <= 3:
            print("Young!")
        elif self.dog_age <= 7:
            print("Adult!")
        else:
            print("Old")

    def check_if_dog_is_old(self):
        """
        DOCSTRING:
        Checks if dog is old
        if dog is younger than 3 years it will show young
        if dog is younger than 7 years it will show adult
        if dog is older than 7 years it will show old
        :param self:
        :return: None
        """
        if self.age <= 3:
            print("young!")
        elif self.age <= 7:
            print("Adult")
        elif self.age > 7:
            print("Old")

    @staticmethod
    def bark():
        print("Woof!!!")


mydog = Dog("Raja", 7, "White")
mydog.check_if_dog_is_old()

mydog.check_if_dog_is_old_by_class_variables()
mydog.bark()
