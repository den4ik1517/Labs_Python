from Models.Insect import Insect

class Hornet(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, venom_level):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.venom_level = venom_level

