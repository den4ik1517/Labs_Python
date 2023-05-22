from abc import ABC

class Insect(ABC):
    def __init__(self, name, number_of_legs, has_wings):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings

    def __str__(self):
        return f"Insect: {self.name}, Legs: {self.number_of_legs}, Wings: {self.has_wings}"


