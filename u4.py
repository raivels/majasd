class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hi, my name is {self.name}")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Today is my {self.age}th birthday!")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Starting the engine...")

    def stop_engine(self):
        print("Stopping the engine...")

    def honk(self):
        print("Honk honk!")


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying...")

    def take_exam(self):
        print(f"{self.name} is taking an exam...")

    def graduate(self):
        if self.gpa >= 2.0:
            print(f"{self.name} is graduating!")
        else:
            print(f"{self.name} needs to improve their GPA.")
            .
