"""
Lab 01 - Simple Calculator
Software Engineering

This program demonstrates:
- Functions
- User input
- Conditional statements
- Exception handling
- Basic software testing
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a + b


def divide(a, b):
    """Return the division of two numbers."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculator():
    """Run the calculator application."""

    print("===================================")
    print("       SOFTWARE ENGINEERING")
    print("          SIMPLE CALCULATOR")
    print("===================================")

    while True:

        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            continue

        try:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                try:
                    result = divide(num1, num2)
                except ValueError as error:
                    print("Error:", error)
                    continue

            print("\nResult:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
