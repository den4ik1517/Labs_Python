from Models.Insect import Insect

class Bee(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, produces_honey):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.produces_honey = produces_honey


