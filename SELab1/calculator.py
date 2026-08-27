"""
Lab 01 - Enhanced Simple Calculator
Software Engineering

This program demonstrates:
- Functions with type hints
- User input handling
- Conditional statements
- Exception handling
- Comprehensive mathematical operations
- Basic software testing
"""

import math
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the difference between two numbers.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Returns:
        Difference of a - b
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the product of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Return the division of two numbers.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Result of a / b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def modulus(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the remainder of division (modulus operation).

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Remainder of a % b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot perform modulus with zero divisor.")

    return a % b


def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return a raised to the power of b.

    Args:
        a: Base
        b: Exponent

    Returns:
        Result of a ** b
    """
    return a ** b


def square_root(a: Union[int, float]) -> float:
    """
    Return the square root of a number.

    Args:
        a: The number to find the square root of

    Returns:
        Square root of a

    Raises:
        ValueError: If a is negative
    """
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")

    return math.sqrt(a)


def factorial(a: Union[int, float]) -> int:
    """
    Return the factorial of a number.

    Args:
        a: The number to compute factorial of

    Returns:
        Factorial of a

    Raises:
        ValueError: If a is not a non-negative integer
    """
    if not isinstance(a, int) or a < 0:
        raise ValueError("Factorial requires a non-negative integer.")

    return math.factorial(a)


def calculator() -> None:
    """
    Run the interactive calculator application.

    Displays a menu with operations and processes user input.
    Continues until user selects exit option.
    """

    print("===================================")
    print("       ENHANCED SIMPLE CALCULATOR")
    print("    Software Engineering Lab 01")
    print("===================================")

    while True:

        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Factorial")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "9":
            print("\nThank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice. Please select 1-9.")
            continue

        try:
            # Operations requiring two inputs
            if choice in ["1", "2", "3", "4", "5", "6"]:
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
                    try:
                        result = modulus(num1, num2)
                    except ValueError as error:
                        print("Error:", error)
                        continue

                elif choice == "6":
                    result = power(num1, num2)

            # Operations requiring one input
            else:
                num1 = float(input("Enter number: "))

                if choice == "7":
                    try:
                        result = square_root(num1)
                    except ValueError as error:
                        print("Error:", error)
                        continue

                elif choice == "8":
                    try:
                        result = factorial(num1)
                    except ValueError as error:
                        print("Error:", error)
                        continue

            print("\nResult:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
