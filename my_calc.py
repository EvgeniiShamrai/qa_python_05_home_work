def sum(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
