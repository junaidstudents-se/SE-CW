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
    return a * b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def percentage(value, percent):
    """Return the percentage amount of a value."""
    return value * (percent / 100)


def divide(a, b):
    """Return the division of two numbers."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculator():
    """Run the calculator application."""

    print("===================================")
    print("       SOFTWARE ENGINEERING Syed Muhammad Junaid Hassan")
    print("          SIMPLE CALCULATOR 15741")
    print("===================================")

    while True:

        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Percentage")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            print("\nThank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please select 1-7.")
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

            elif choice == "5":
                result = power(num1, num2)

            elif choice == "6":
                result = percentage(num1, num2)

            print("\nResult:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
