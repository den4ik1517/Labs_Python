from managers.insect_manager import InsectManager
from models.bee import Bee
from models.butterfly import Butterfly
from models.hornet import Hornet
from models.mosquito import Mosquito

def main():
    insect_manager = InsectManager()
    insect_manager.add_insects(
        Mosquito("Mosquito", 6, True, True, True),
        Hornet("Hornet", 6, True, True, 5),
        Bee("Bee", 6, True, False, True),
        Butterfly("Butterfly", 6, True, False, True, 10))

    print("Insects with 6 legs:")
    print(*insect_manager.find_all_with_number_of_legs(6), sep=" | ")

    print("\nInsects with wings:")
    for insect in insect_manager.find_all_with_wings():
        print(insect)

    results = [f"{index}: {insect.find_name()}: {insect}" for index, insect in enumerate(insect_manager, start=1)
               for insect, name in zip(insect_manager, map(lambda x: x.find_name(), insect_manager))]
    print("\nName of insects:")
    print(*results, sep=" | ")

    insect = Mosquito("Mosquito", 6, True, True, True)
    attributes = insect.get_attributes_by_type(int)
    print("\nAttributes with int type:")
    print(*attributes.values(), sep=" | ")

    all_condition = all(insect.can_inject_poison() for insect in insect_manager)
    any_condition = any(insect.survive_over_winter() for insect in insect_manager)

    conditions_dict = {"all": all_condition, "any": any_condition}
    print("\nConditions:")
    print(conditions_dict)

if __name__ == "__main__":
    main()

