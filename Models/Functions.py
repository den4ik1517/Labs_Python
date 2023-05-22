from Managers.InsectManager import InsectManager
from Models.Bee import Bee
from Models.Butterfly import Butterfly
from Models.Hornet import Hornet
from Models.Mosquito import Mosquito

insects = [
    Mosquito("Mosquito", 6, True, True, True),
    Hornet("Hornet", 6, True, True, 5),
    Bee("Bee", 6, True, False, True),
    Butterfly("Butterfly", 6, True, False, True, 10)
]

insect_manager = InsectManager("Insect Manager", 0, False)
for insect in insects:
    insect_manager.add_insect(insect)

print("Insects with 6 legs:")
for insect in insect_manager.find_all_with_number_of_legs(6):
    print(insect)

print("\nInsects with wings:")
for insect in insect_manager.find_all_with_wings():
    print(insect)
