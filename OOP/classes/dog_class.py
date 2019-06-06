class Dog:
    def __init__(self, name, age, spots, breed=None):
        """
        DOCSTRING:
        This is like constructor in other programming languages
        :param name:String
        :param age:Integer
        :param spots:Boolean
        """
        self.name = name
        self.age = age
        self.spots = spots
        self.breed = breed

    def call_dog(self):
        print("Calling {}".format(self.name))

    def tell_your_age(self):
        print("I am a doggo and I am {} years old".format(self.age))

    def add_breed(self, breed):
        self.breed = breed

    def check_if_spots_are_present(self):
        if self.spots:
            return ""
        else:
            return "no"

    def show_me(self):
        print(f"I am doggo who is called as {self.name}\n"
              f"Whose age is {self.age}\n"
              f"and have{self.check_if_spots_are_present()}", end="")
        print(" spots\n"
              f"And belongs to {self.breed} breed")


raja = Dog("Raja", 7, False)
other = Dog("Other", 1, True)
jennie = Dog("Jennie", 4, False)

raja.call_dog()
jennie.call_dog()
raja.tell_your_age()
jennie.tell_your_age()

raja.add_breed("Pikachu")
jennie.add_breed("Bulbasaour")

raja.show_me()
jennie.show_me()
other.show_me()