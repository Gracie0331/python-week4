class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old, and I identify as {self.gender}.")

person = Person("John Doe", 30, "male")
person.introduce()
