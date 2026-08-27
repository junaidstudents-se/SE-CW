"""
Demonstration file showing the Enhanced Calculator in action.
Run this file to test all calculator functions.
"""

from SELab1.calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    square_root,
    factorial,
)


def demonstrate_operations() -> None:
    """Demonstrate all calculator operations with example outputs."""

    print("=" * 60)
    print("ENHANCED CALCULATOR DEMONSTRATION")
    print("=" * 60)

    # Addition
    print("\n1. ADDITION")
    print(f"   add(10, 5) = {add(10, 5)}")
    print(f"   add(-10, -5) = {add(-10, -5)}")
    print(f"   add(1.5, 2.3) = {add(1.5, 2.3)}")

    # Subtraction
    print("\n2. SUBTRACTION")
    print(f"   subtract(10, 5) = {subtract(10, 5)}")
    print(f"   subtract(10, -5) = {subtract(10, -5)}")
    print(f"   subtract(5.5, 2.2) = {subtract(5.5, 2.2)}")

    # Multiplication
    print("\n3. MULTIPLICATION")
    print(f"   multiply(10, 5) = {multiply(10, 5)}")
    print(f"   multiply(-10, 5) = {multiply(-10, 5)}")
    print(f"   multiply(2.5, 3.2) = {multiply(2.5, 3.2)}")

    # Division
    print("\n4. DIVISION")
    print(f"   divide(10, 5) = {divide(10, 5)}")
    print(f"   divide(5, 2) = {divide(5, 2)}")
    print(f"   divide(-10, 2) = {divide(-10, 2)}")

    # Modulus
    print("\n5. MODULUS")
    print(f"   modulus(10, 3) = {modulus(10, 3)}")
    print(f"   modulus(15, 4) = {modulus(15, 4)}")
    print(f"   modulus(-10, 3) = {modulus(-10, 3)}")

    # Power
    print("\n6. POWER")
    print(f"   power(2, 3) = {power(2, 3)}")
    print(f"   power(10, 2) = {power(10, 2)}")
    print(f"   power(2, -1) = {power(2, -1)}")
    print(f"   power(4, 0.5) = {power(4, 0.5)}")

    # Square Root
    print("\n7. SQUARE ROOT")
    print(f"   square_root(4) = {square_root(4)}")
    print(f"   square_root(9) = {square_root(9)}")
    print(f"   square_root(2) = {square_root(2):.4f}")
    print(f"   square_root(100) = {square_root(100)}")

    # Factorial
    print("\n8. FACTORIAL")
    print(f"   factorial(0) = {factorial(0)}")
    print(f"   factorial(5) = {factorial(5)}")
    print(f"   factorial(10) = {factorial(10)}")
    print(f"   factorial(5.0) = {factorial(5.0)}")

    print("\n" + "=" * 60)
    print("All demonstrations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_operations()
