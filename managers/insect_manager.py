from decorators.key_arguments_to_file import log_arguments
from decorators.method_and_exception_to_file import log_exceptions

class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insects(self, *insects):
        for insect in insects:
            self.insects.append(insect)

    @log_arguments
    def find_all_with_number_of_legs(self, number_of_legs):
        return filter(lambda x: x.number_of_legs == number_of_legs, self.insects)

    @log_exceptions
    def find_all_with_wings(self):
        result = filter(lambda x: x.has_wings, self.insects)
        if not result:
            raise False
        return result

    def __len__(self):
        return len(self.insects)

    def __getitem__(self, index):
        return self.insects[index]

    def __iter__(self):
        return iter(self.insects)
