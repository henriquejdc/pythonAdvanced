# Timing
import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper


@timed
def myfunction(x):
    result = 1
    for number in range(1, x):
        result += 1
    return result


print(myfunction(100))
