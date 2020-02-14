
def upper(text):
    return text.upper()


def lower(text):
    return text.lower()


def case(function):
    # storing the function in a variable
    greeting = function("Hi, I am created by a function passed as an argument.")
    print(greeting)


case(upper)
case(lower)
