# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"

# Taking input
try:
    a = (input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    calc = Calculator()

    if operation == "add":
        print("Result:", calc.add(a, b))
    elif operation == "subtract":
        print("Result:", calc.subtract(a, b))
    elif operation == "multiply":
        print("Result:", calc.multiply(a, b))
    elif operation == "divide":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid operation! Choose from add, subtract, multiply, divide.")

except ValueError:
    print("Invalid input! Please enter numeric values for a and b.")
