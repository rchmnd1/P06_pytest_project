from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    def test_add_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 4
        assert result == expected
    def test_add_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -3
        assert result == expected
    def test_subtract(self):
        # arrange
        a = 10
        b = 5
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 5
        assert result == expected
    def test_multiply(self):
        # arrange
        a = 9
        b = 9
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 81
        assert result == expected
    def test_divide(self):
        # arrange
        a = 10
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5
        assert result == expected
    def test_divide_2(self):
        # arrange
        a = 10
        b = 0
        cal = Calculator()

        # act
        try:
            result = cal.divide(a, b)
        except ZeroDivisionError as e:
            result = e

        # assert
        expected = ZeroDivisionError("Division by zero error")
        assert isinstance(result, ZeroDivisionError)
        assert str(result) == str(expected)
