class Insect:
    __instance = None

    def __init__(self, name="", number_of_legs=6, has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    @staticmethod
    def get_instance():
        if not Insect.__instance:
            Insect.__instance = Insect()
        return Insect.__instance

    @staticmethod
    def is_poisonous():
        return False

    def hibernate(self):
        self.is_sleeping = False

    def wake_up(self):
        self.is_sleeping = False

    def __str__(self):
        return f"Insect(name={self.name}, number_of_legs={self.number_of_legs}, has_wings={self.has_wings}, is_dangerous={self.is_dangerous}, is_sleeping={self.is_sleeping})"


if __name__ == '__main__':
    insects = [
        Insect("Bee", 6, True, True, True),
    ]

    for insect in insects:
        print(insect)
