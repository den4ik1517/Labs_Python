from models.insect import Insect

class Butterfly(Insect):
    def __init__(self, name, number_of_legs, has_wings, can_fly, colorful, lifespan):
        """
        Initializes the Butterfly object with a name, number of legs, wings, ability to fly, colorfulness, and lifespan.
        It calls the superclass's __init__ method to initialize common attributes.
        The favorite_food_set is set to the return value of the get_favorite_food method.
        """
        super().__init__(name, number_of_legs, has_wings)
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.can_fly = can_fly
        self.colorful = colorful
        self.lifespan = lifespan

    def survive_over_winter(self):
        """
        Implements the abstract method from the superclass.
        Specifies whether the Butterfly can survive over winter.
        """
        pass

    def can_inject_poison(self):
        """
        Implements the abstract method from the superclass.
        Specifies whether the Butterfly can inject poison.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the Butterfly object.
        """
        return f"name:{self.name}, number_of_legs:{self.number_of_legs}," \
               f" has_wings:{self.has_wings}, can_fly:{self.can_fly}, lifespan:{self.lifespan}"
