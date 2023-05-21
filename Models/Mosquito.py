from Models.Insect import Insect

class Mosquito(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, max_speed):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.max_speed = max_speed

