from abc import abstractmethod, ABC

class Insect(ABC):
    def __init__(self, name, number_of_legs, has_wings):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.data_set = set()
        self.favorite_food_set = set()

    def get_favorite_food(self):
        pass

    def __iter__(self):
        return iter(self.favorite_food_set)

    def __len__(self):
        return len(self.favorite_food_set)

    def __getitem__(self, index):
        return list(self.favorite_food_set)[index]

    def find_name(self):
        return self.name

    @abstractmethod
    def can_inject_poison(self):
        pass

    @abstractmethod
    def survive_over_winter(self):
        pass

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type) and type(value) is int}
