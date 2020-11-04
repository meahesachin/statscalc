import math
from Calculator import addition, subtraction


def multiplication(a, b):
    c = float(a)*float(b)
    return float(c)


def division(a, b):
    c = float(a)/float(b)
    return float(c)


def squared(a):
    c = float(a) ** 2
    return c


def squareroot(a):
    c = math.sqrt(a)
    return float(c)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction.subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        if float(b) == 0:
            return 0
        self.result = division(a, b)
        return format(self.result, '.9f')

    def square(self, a):
        self.result = squared(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(int(a))
        fmt = ""
        if self.result.is_integer():
            fmt = ".1f"
        else:
            fmt = ".8f"
        return format(self.result, fmt)


