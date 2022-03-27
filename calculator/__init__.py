"""
docstring: a moduLe for Calculator
"""


class Calculator:
    """
    docstring: a Calculator class
    """

    def __init__(self, num1, sign, num2):
        self.num1 = num1
        self.sign = sign
        self.num2 = num2

    def get_result(self):
        """
               docstring: get the result of the calculator
        """
        if self.sign == '+':
            result = self.num1 + self.num2
        elif self.sign == '-':
            result = self.num1 - self.num2
        elif self.sign == '*':
            result = self.num1 * self.num2
        elif self.sign == '/':
            try:
                result = self.num1 / self.num2
            except ZeroDivisionError:
                print("zero cannot to be the division")
        else:
            print("Input the wrong operator！")
        return result

    def get_sign(self):
        """
               docstring:get the operator
        """
        return self.sign
