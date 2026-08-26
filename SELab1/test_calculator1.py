import pytest

from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import power
from calculator import percentage
from calculator import divide


# -------------------------------
# PASSING TESTS
# -------------------------------

def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_power():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_percentage():
    assert percentage(200, 10) == 20


def test_percentage_zero_percent():
    assert percentage(500, 0) == 0


def test_percentage_negative_percent():
    assert percentage(200, -10) == -20


def test_divide():
    assert divide(10, 5) == 2


# -------------------------------
# INTENTIONALLY FAILING TESTS
# -------------------------------

def test_add_wrong_result():
    assert add(10, 5) == 20


def test_subtract_wrong_result():
    assert subtract(10, 5) == 10


def test_multiply_wrong_result():
    assert multiply(10, 5) == 40


def test_divide_wrong_result():
    assert divide(10, 5) == 3


def test_negative_number_wrong_result():
    assert add(-10, -5) == 10


def test_decimal_wrong_result():
    assert divide(5, 2) == 3


# -------------------------------
# EXCEPTION TEST
# -------------------------------

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
