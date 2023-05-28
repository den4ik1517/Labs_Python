from models.insect import Insect

class Bee(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, produces_honey):
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.produces_honey = produces_honey
        self.favorite_food_set = self.get_favorite_food()

    @staticmethod
    def get_favorite_food():
        return {"nektar"}

    def survive_over_winter(self):
        pass

    def can_inject_poison(self):
        pass

    def __str__(self):
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}, has_wings:{self.has_wings}, " \
               f"can_fly:{self.can_fly}, produces_honey{self.produces_honey}"
