from decorators.logged import logged
from exceptions.eat_exception import EatException
from managers.insect_manager import InsectManager
from models.bee import Bee
from models.butterfly import Butterfly
from models.hornet import Hornet
from models.mosquito import Mosquito
import logging

def main():
    # Create an instance of the InsectManager class
    insect_manager = InsectManager()

    # Add instances of different insect models to the insect manager
    insect_manager.add_insects(
        Mosquito("Mosquito", 6, True, False, True),
        Hornet("Hornet", 6, True, False, True),
        Bee("Bee", 6, True, False, False),
        Butterfly("Butterfly", 6, True, False, False, True))

    # Modify an insect's attribute to trigger the exception
    insect_manager.insects[0].can_eat = False

    # Print insects with 6 legs
    print("Insects with 6 legs:")
    print(*insect_manager.find_all_with_number_of_legs(6), sep=" | ")

    # Print insects with wings
    print("\nInsects with wings:")
    for insect in insect_manager.find_all_with_wings():
        print(insect)

    # Define a function that is decorated with the 'logged' decorator
    @logged(EatException, "file")
    def write_to_file(message):
        if message == "0":
            raise EatException("The insect wants to eat")
    try:
        # Call the decorated function
        write_to_file("0")
    except EatException as e:
        # Handle the exception by writing it to a file
        e.write_to_file()


if __name__ == "__main__":
    main()
