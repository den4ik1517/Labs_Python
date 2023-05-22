from Models.Insect import Insect

class Butterfly(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, colorful, lifespan):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.colorful = colorful
        self.lifespan = lifespan