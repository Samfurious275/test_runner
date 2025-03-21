# calculator.py

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Welcome to the Simple Calculator!")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        operation = int(input("Select an operation (1/2/3/4): "))
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 1:
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == 2:
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == 3:
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == 4:
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation selected.")
    except ValueError as e:
        print(f"Error: {e}")
