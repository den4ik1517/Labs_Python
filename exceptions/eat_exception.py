import logging
from decorators.logged import logged


class EatException(Exception):
    def __init__(self, message):
        self.message = message

    def write_to_file(self):
        """
        Writes the exception message to a file.
        This method is intended to be overridden in subclasses to provide specific file writing functionality.
        """
        pass


@logged(EatException, "file")
def write_to_file(message):
    """
    A function that writes a message to a file.
    If the message is "0", it raises an EatException.
    This function is decorated with `logged`, which logs exceptions to a file.
    """
    if message == "0":
        with open("exception.txt", "a") as file:
            file.write("EatException: The insect cannot eat.\n")
