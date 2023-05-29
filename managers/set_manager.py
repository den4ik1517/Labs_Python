from models.bee import Bee
from models.butterfly import Butterfly
from models.hornet import Hornet
from models.mosquito import Mosquito

class SM:
    def __init__(self, rm_manager):
        self.rm_manager = rm_manager
        self.current_index = 0

    def __iter__(self):
        self.current_index = 0
        return self

    def __len__(self):
        return sum(len(obj.get_favorite_food()) for obj in self.rm_manager)

    def __getitem__(self, index):
        for obj in self.rm_manager:
            favorite_food_set = obj.get_favorite_food()
            if index < len(favorite_food_set):
                return list(favorite_food_set)[index]
            index -= len(favorite_food_set)
        raise IndexError("Index out of range")

    def __next__(self):
        if self.current_index >= len(self):
            raise StopIteration
        for obj in self.rm_manager:
            favorite_food_set = obj.get_favorite_food()
            if self.current_index < len(favorite_food_set):
                item = list(favorite_food_set)[self.current_index]
                self.current_index += 1
                return item
        raise StopIteration

def main():
    rm_manager = [
        Butterfly("Butterfly", 6, True, True, "orange", "2 weeks"),
        Mosquito("Mosquito", 6, True, True, True),
        Hornet("Hornet", 6, True, True, 5),
        Bee("Bee", 6, True, False, True)
    ]
    sm = SM(rm_manager)

    print("\nSet elements:")
    print("\nFavorite food Butterfly:", sm[0])
    print("Favorite food Mosquito:", sm[1])
    print("Favorite food Hornet:", sm[2])
    print("Favorite food Bee:", sm[3])
    print("\nSet length:", len(sm))

if __name__ == "__main__":
    main()
