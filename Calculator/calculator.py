import math
from Calculator import addition, subtraction, multiplication, division, squared, squareroot


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
        self.result = multiplication.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division.division(a, b)
        return self.result

    def square(self, a):
        self.result = squared.squared(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot.squareroot(int(a))
        return self.result


