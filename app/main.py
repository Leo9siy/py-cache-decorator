from typing import Callable
new_set = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Callable:
        if (func.__name__, *args) in new_set:
            print("Getting from cache")
            return new_set[(func.__name__, *args)]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            new_set[(func.__name__, *args)] = result
            return result
    return wrapper
