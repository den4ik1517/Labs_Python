from models.insect import Insect

class Hornet(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, venom_level):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.venom_level = venom_level
        self.favorite_food_set = self.get_favorite_food()

    @staticmethod
    def get_favorite_food():
        return {"popeluci"}

    def survive_over_winter(self):
        pass

    def can_inject_poison(self):
        pass

    def __str__(self):
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}, has_wings:{self.has_wings}, " \
               f"can_fly:{self.can_fly}, venom_level{self.venom_level}"
