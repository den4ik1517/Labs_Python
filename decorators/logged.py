import logging


def logged(custom_exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Call the decorated function
                return func(*args, **kwargs)
            except custom_exception as e:
                if mode == "console":
                    # Configure logging to log the exception to the console
                    logging.basicConfig(level=logging.INFO)
                    logging.error(e)
                elif mode == "file":
                    # Configure logging to log the exception to a file
                    logging.basicConfig(level=logging.INFO, filename="exception.log", filemode="a")
                    logging.error(e)
                else:
                    # Raise an exception if an invalid logging mode is provided
                    raise ValueError("Invalid logging mode. Please choose 'console' or 'file'.")
                # Call the write_to_file method of the exception
                e.write_to_file()
        return wrapper
    return decorator
