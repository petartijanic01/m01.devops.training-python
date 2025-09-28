import pytest
from demo_project import calculator


def test_add():
    assert calculator.add(1, 2) == 3


def test_subtract():
    assert calculator.subtract(5, 3) == 2


def test_multiply():
    assert calculator.multiply(3, 4) == 12


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)
