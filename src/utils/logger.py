import logging
from functools import wraps

def logger(func):
    """
    A decorator function to log information about function calls and their results.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that logs function calls and their results.
        """
        logging.info(f"Running {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Finished {func.__name__} with result: {result}")
        
        except Exception as e:
            logging.error(f"Error occurred in {func.__name__}: {e}")
            raise
        
        else:
            return result

    return wrapper