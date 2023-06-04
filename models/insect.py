from abc import abstractmethod, ABC

class Insect(ABC):
    def __init__(self, name, number_of_legs, has_wings):
        """
        Initializes the Insect object with a name, number of legs, and wings.
        It also initializes an empty data_set and favorite_food_set.
        """
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.data_set = set()

    @abstractmethod
    def can_inject_poison(self):
        """
        Abstract method to be implemented by subclasses.
        Returns whether the insect can inject poison.
        """
        pass

    @abstractmethod
    def survive_over_winter(self):
        """
        Abstract method to be implemented by subclasses.
        Returns whether the insect can survive over winter.
        """
        pass
