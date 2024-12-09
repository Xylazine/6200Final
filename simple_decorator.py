from typing import Callable
from functools import wraps

def add_one_if_int(func: Callable[..., int]) -> Callable[..., int]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        result = func(*args, **kwargs)
        if isinstance(result, int):  # Check if the result is an integer
            result += 1
        return result
    return wrapper


def logger(func: Callable[..., int])-> Callable[..., int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function call
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        # Call the original function
        result = func(*args, **kwargs)
        # Log the result
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


@logger
@add_one_if_int
def return_int_value(value: int=0)-> int:
    return value


return_int_value()
