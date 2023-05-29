from models.insect import Insect

class Mosquito(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, max_speed):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.max_speed = max_speed
        self.favorite_food_set = self.get_favorite_food()

    @staticmethod
    def get_favorite_food():
        return {"blood"}

    def survive_over_winter(self):
        pass

    def can_inject_poison(self):
        pass

    def __str__(self):
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}," \
               f" has_wings:{self.has_wings}, can_fly:{self.can_fly}, max_speed{self.max_speed}"
