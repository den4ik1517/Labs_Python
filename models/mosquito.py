from models.insect import Insect

class Mosquito(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, max_speed):
        """
        Initializes the Mosquito object with a name, number of legs, wings, ability to fly, and maximum speed.
        It calls the superclass's __init__ method to initialize common attributes.
        The favorite_food_set is set to the return value of the get_favorite_food method.
        """
        super().__init__(name, number_of_legs, has_wings)
        self.can_fly = can_fly
        self.max_speed = max_speed

    def survive_over_winter(self):
        """
        Implements the abstract method from the superclass.
        Specifies whether the Mosquito can survive over winter.
        """
        pass

    def can_inject_poison(self):
        """
        Implements the abstract method from the superclass.
        Specifies whether the Mosquito can inject poison.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the Mosquito object.
        """
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}," \
               f" has_wings:{self.has_wings}, can_fly:{self.can_fly}, max_speed:{self.max_speed}"
