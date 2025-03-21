# tests/test_calculator.py

# Import the calculator module (assuming it's named calculator.py)
import calculator

# Test addition
def test_add():
    assert calculator.add(2, 3) == 5

# Test subtraction
def test_subtract():
    assert calculator.subtract(5, 3) == 2

# Test multiplication
def test_multiply():
    assert calculator.multiply(2, 3) == 6

# Test division
def test_divide():
    assert calculator.divide(6, 3) == 2
