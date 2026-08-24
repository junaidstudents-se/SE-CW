"""
Lab 01 - Calculator Tests

These tests verify the functionality
of the calculator functions.
"""

import pytest

from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_add_negative_numbers():
    assert add(-10, -5) == -15


def test_divide_decimal_numbers():
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
