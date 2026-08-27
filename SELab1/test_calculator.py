"""
Comprehensive test suite for the Enhanced Calculator

Tests cover:
- Basic operations (add, subtract, multiply, divide, modulus, power)
- Single-input operations (square root, factorial)
- Edge cases (negative numbers, decimals, boundaries, zeros)
- Exception handling and error conditions
"""

import pytest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    square_root,
    factorial,
)


# ========================================
# ADDITION TESTS
# ========================================


class TestAddition:
    """Test cases for addition operation."""

    def test_add_positive_integers(self) -> None:
        """Test addition of positive integers."""
        assert add(10, 5) == 15

    def test_add_negative_integers(self) -> None:
        """Test addition of negative integers."""
        assert add(-10, -5) == -15

    def test_add_mixed_signs(self) -> None:
        """Test addition with mixed positive and negative numbers."""
        assert add(10, -5) == 5
        assert add(-10, 5) == -5

    def test_add_decimals(self) -> None:
        """Test addition of decimal numbers."""
        assert add(1.5, 2.3) == pytest.approx(3.8)
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_zero(self) -> None:
        """Test addition with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_large_numbers(self) -> None:
        """Test addition of large numbers."""
        assert add(1000000, 2000000) == 3000000


# ========================================
# SUBTRACTION TESTS
# ========================================


class TestSubtraction:
    """Test cases for subtraction operation."""

    def test_subtract_positive_integers(self) -> None:
        """Test subtraction of positive integers."""
        assert subtract(10, 5) == 5

    def test_subtract_negative_integers(self) -> None:
        """Test subtraction with negative integers."""
        assert subtract(-10, -5) == -5
        assert subtract(-5, -10) == 5

    def test_subtract_mixed_signs(self) -> None:
        """Test subtraction with mixed positive and negative numbers."""
        assert subtract(10, -5) == 15
        assert subtract(-10, 5) == -15

    def test_subtract_decimals(self) -> None:
        """Test subtraction of decimal numbers."""
        assert subtract(5.5, 2.2) == pytest.approx(3.3)

    def test_subtract_zero(self) -> None:
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0

    def test_subtract_same_number(self) -> None:
        """Test subtracting a number from itself."""
        assert subtract(5, 5) == 0


# ========================================
# MULTIPLICATION TESTS
# ========================================


class TestMultiplication:
    """Test cases for multiplication operation."""

    def test_multiply_positive_integers(self) -> None:
        """Test multiplication of positive integers."""
        assert multiply(10, 5) == 50

    def test_multiply_negative_integers(self) -> None:
        """Test multiplication with negative integers."""
        assert multiply(-10, -5) == 50
        assert multiply(-10, 5) == -50

    def test_multiply_decimals(self) -> None:
        """Test multiplication of decimal numbers."""
        assert multiply(2.5, 3.2) == pytest.approx(8.0)

    def test_multiply_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0

    def test_multiply_by_one(self) -> None:
        """Test multiplication by one."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5

    def test_multiply_large_numbers(self) -> None:
        """Test multiplication of large numbers."""
        assert multiply(1000, 2000) == 2000000


# ========================================
# DIVISION TESTS
# ========================================


class TestDivision:
    """Test cases for division operation."""

    def test_divide_positive_integers(self) -> None:
        """Test division of positive integers."""
        assert divide(10, 5) == 2

    def test_divide_decimals(self) -> None:
        """Test division resulting in decimals."""
        assert divide(5, 2) == pytest.approx(2.5)

    def test_divide_negative_numbers(self) -> None:
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self) -> None:
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0

    def test_divide_by_one(self) -> None:
        """Test division by one."""
        assert divide(5, 1) == 5


# ========================================
# MODULUS TESTS
# ========================================


class TestModulus:
    """Test cases for modulus operation."""

    def test_modulus_positive_integers(self) -> None:
        """Test modulus of positive integers."""
        assert modulus(10, 3) == 1
        assert modulus(15, 4) == 3

    def test_modulus_negative_numbers(self) -> None:
        """Test modulus with negative numbers."""
        assert modulus(-10, 3) == 2
        assert modulus(10, -3) == -2

    def test_modulus_zero_dividend(self) -> None:
        """Test modulus with zero as dividend."""
        assert modulus(0, 5) == 0

    def test_modulus_by_zero_raises_error(self) -> None:
        """Test that modulus by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot perform modulus with zero divisor"):
            modulus(10, 0)

    def test_modulus_decimals(self) -> None:
        """Test modulus with decimal numbers."""
        result = modulus(5.5, 2.2)
        assert result == pytest.approx(1.1, abs=1e-9)

    def test_modulus_equal_numbers(self) -> None:
        """Test modulus of equal numbers."""
        assert modulus(5, 5) == 0


# ========================================
# POWER TESTS
# ========================================


class TestPower:
    """Test cases for power operation."""

    def test_power_positive_integers(self) -> None:
        """Test power of positive integers."""
        assert power(2, 3) == 8
        assert power(10, 2) == 100

    def test_power_negative_exponent(self) -> None:
        """Test power with negative exponent."""
        assert power(2, -1) == pytest.approx(0.5)
        assert power(10, -2) == pytest.approx(0.01)

    def test_power_zero_exponent(self) -> None:
        """Test power with zero exponent."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_negative_base(self) -> None:
        """Test power with negative base."""
        assert power(-2, 2) == 4
        assert power(-2, 3) == -8

    def test_power_decimal_exponent(self) -> None:
        """Test power with decimal exponent."""
        assert power(4, 0.5) == pytest.approx(2)

    def test_power_zero_base(self) -> None:
        """Test power with zero base."""
        assert power(0, 5) == 0

    def test_power_base_one(self) -> None:
        """Test power with base of one."""
        assert power(1, 100) == 1


# ========================================
# SQUARE ROOT TESTS
# ========================================


class TestSquareRoot:
    """Test cases for square root operation."""

    def test_square_root_perfect_squares(self) -> None:
        """Test square root of perfect squares."""
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(16) == 4
        assert square_root(100) == 10

    def test_square_root_decimals(self) -> None:
        """Test square root of decimal numbers."""
        assert square_root(2.25) == pytest.approx(1.5)

    def test_square_root_zero(self) -> None:
        """Test square root of zero."""
        assert square_root(0) == 0

    def test_square_root_one(self) -> None:
        """Test square root of one."""
        assert square_root(1) == 1

    def test_square_root_negative_raises_error(self) -> None:
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
            square_root(-4)

    def test_square_root_non_perfect_square(self) -> None:
        """Test square root of non-perfect squares."""
        assert square_root(5) == pytest.approx(2.236, rel=1e-3)
        assert square_root(10) == pytest.approx(3.162, rel=1e-3)

    def test_square_root_large_number(self) -> None:
        """Test square root of large numbers."""
        assert square_root(1000000) == 1000


# ========================================
# FACTORIAL TESTS
# ========================================


class TestFactorial:
    """Test cases for factorial operation."""

    def test_factorial_small_integers(self) -> None:
        """Test factorial of small integers."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(5) == 120

    def test_factorial_larger_integers(self) -> None:
        """Test factorial of larger integers."""
        assert factorial(10) == 3628800

    def test_factorial_float_whole_numbers(self) -> None:
        """Test factorial with float that are whole numbers."""
        assert factorial(5.0) == 120
        assert factorial(3.0) == 6

    def test_factorial_negative_raises_error(self) -> None:
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial requires a non-negative integer"):
            factorial(-5)

    def test_factorial_decimal_raises_error(self) -> None:
        """Test that factorial of non-integer decimal raises ValueError."""
        with pytest.raises(ValueError, match="Factorial requires a non-negative integer"):
            factorial(5.5)
        with pytest.raises(ValueError, match="Factorial requires a non-negative integer"):
            factorial(3.14)


# ========================================
# INTEGRATION TESTS
# ========================================


class TestIntegration:
    """Integration tests combining multiple operations."""

    def test_combined_operations_1(self) -> None:
        """Test combining multiple operations."""
        # (10 + 5) * 2 = 30
        result = multiply(add(10, 5), 2)
        assert result == 30

    def test_combined_operations_2(self) -> None:
        """Test combining division and subtraction."""
        # (20 - 5) / 3 ≈ 5
        result = divide(subtract(20, 5), 3)
        assert result == pytest.approx(5)

    def test_combined_operations_3(self) -> None:
        """Test combining power and multiplication."""
        # 2^3 * 5 = 8 * 5 = 40
        result = multiply(power(2, 3), 5)
        assert result == 40

    def test_combined_operations_4(self) -> None:
        """Test combining square root and power."""
        # sqrt(16) ^ 2 = 4 ^ 2 = 16
        result = power(square_root(16), 2)
        assert result == 16
