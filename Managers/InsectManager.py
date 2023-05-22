from Models.Insect import Insect

class InsectManager(Insect):
    def __init__(self, name, number_of_legs, has_wings):
        super().__init__(name, number_of_legs, has_wings)
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.insects = []

    def add_insect(self, insect):
        self.insects.append(insect)

    def find_all_with_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.number_of_legs == number_of_legs]

    def find_all_with_wings(self):
        return [insect for insect in self.insects if insect.has_wings]