from models.insect import Insect

class Butterfly(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, colorful, lifespan):
        super().__init__(name, number_of_legs, has_wings)
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.can_fly = can_fly
        self.colorful = colorful
        self.lifespan = lifespan
        self.favorite_food_set = self.get_favorite_food()

    @staticmethod
    def get_favorite_food():
        return {"flowers"}

    def survive_over_winter(self):
        pass

    def can_inject_poison(self):
        pass

    def __str__(self):
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}," \
               f" has_wings:{self.has_wings}, can_fly:{self.can_fly}, lifespan:{self.lifespan}"
