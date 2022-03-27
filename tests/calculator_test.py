"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator(0,'-',0)
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator(0,'+',0)
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator(2,'+',3)
    calc2 = Calculator(3,'+',3)
    assert calc1.get_result() == 5
    assert calc2.get_result() == 6


def test_calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator(1,'+',1)
    assert calculator.get_result() == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator(2,'-',1)
    assert calculator.get_result() == 1

def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    calculator = Calculator(2,'*',2)
    assert calculator.get_result() == 4

def test_calculator_divid_method():
    """Testing the Calculator Division"""
    calculator = Calculator(2,'/',2)
    assert calculator.get_result() == 1
