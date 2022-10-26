# Decorators


def mydecorator(function):

    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function!")
        return return_value

    return wrapper


@mydecorator
def hello(person):
    return f"Hello {person}!"


print(hello("Henrique"))
