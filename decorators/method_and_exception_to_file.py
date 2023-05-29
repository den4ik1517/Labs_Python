def log_exceptions(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            if e is False:
                with open('exceptions_log.txt', 'a+') as file:
                    file.seek(0)
                    has_data = bool(file.read(1))
                    file.seek(0, 2)
                    if not has_data:
                        file.write("Exceptions Log:\n")
                    file.write(f"Method: {self.__class__.__name__}.{func.__name__}\n")
                    file.write(f"Exception: {type(e).__name__}: {str(e)}\n")
            raise e

    return wrapper