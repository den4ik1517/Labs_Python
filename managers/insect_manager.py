class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insects(self, *insects):
        """
        Adds the given insects to the list of insects managed by the InsectManager.
        """
        for insect in insects:
            self.insects.append(insect)

    def find_all_with_number_of_legs(self, number_of_legs):
        """
        Returns all insects with the specified number of legs.
        This method is decorated with `log_arguments`, which logs the function name and its arguments to a file.
        """
        return filter(lambda x: x.number_of_legs == number_of_legs, self.insects)

    def find_all_with_wings(self):
        """
        Returns all insects that have wings.
        """
        return filter(lambda x: x.has_wings, self.insects)
