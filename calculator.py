from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def operate(self, num1, num2):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Addition(Operation):
    def operate(self, num1, num2):
        real_sum = num1.real + num2.real
        imag_sum = num1.imag + num2.imag
        return complex(real_sum, imag_sum)

    def __str__(self):
        return "Addition"


class Multiplication(Operation):
    def operate(self, num1, num2):
        real_mul = num1.real * num2.real - num1.imag * num2.imag
        imag_mul = num1.real * num2.imag + num1.imag * num2.real
        return complex(real_mul, imag_mul)

    def __str__(self):
        return "Multiplication"


class Division(Operation):
    def operate(self, num1, num2):
        try:
            denominator = num2.real ** 2 + num2.imag ** 2
            real_div = (num1.real * num2.real + num1.imag * num2.imag) / denominator
            imag_div = (num1.imag * num2.real - num1.real * num2.imag) / denominator
            return complex(real_div, imag_div)
        except ZeroDivisionError:
            return None

    def __str__(self):
        return "Division"


class ComplexCalculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, num1, num2):
        return self.operation.operate(num1, num2)

    def __str__(self):
        return str(self.operation)