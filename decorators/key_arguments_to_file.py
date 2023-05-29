def log_arguments(func):
    def wrapper(self, *args, **kwargs):
        with open('arguments_log.txt', 'a') as file:
            file.write(f"Method: {self.__class__.__name__}.{func.__name__}\n")

            for arg_name, arg_value in kwargs.items():
                file.write(f"{arg_name}={arg_value}\n")

            return func(self, *args, **kwargs)

    return wrapper