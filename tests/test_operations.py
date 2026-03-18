"""
Unit tests for calculator operations module.
Tests all basic arithmetic operations.
"""

import pytest
from app.operations import add, subtract, multiply, divide


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5

    def test_add_mixed_signs(self):
        """Test adding numbers with mixed signs."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert abs(add(0.1, 0.2) - 0.3) < 1e-9

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_type_error(self):
        """Test that TypeError is raised for non-numeric inputs."""
        with pytest.raises(TypeError):
            add("2", 3)
        with pytest.raises(TypeError):
            add(2, "3")
        with pytest.raises(TypeError):
            add(None, 5)


class TestSubtract:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-2, -3) == 1

    def test_subtract_mixed_signs(self):
        """Test subtracting with mixed signs."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0

    def test_subtract_zero(self):
        """Test subtracting with zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_same_number(self):
        """Test subtracting a number from itself."""
        assert subtract(5, 5) == 0

    def test_subtract_type_error(self):
        """Test that TypeError is raised for non-numeric inputs."""
        with pytest.raises(TypeError):
            subtract("5", 3)
        with pytest.raises(TypeError):
            subtract(5, "3")


class TestMultiply:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_signs(self):
        """Test multiplying with mixed signs."""
        assert multiply(2, -3) == -6
        assert multiply(-2, 3) == -6

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4) == 10.0

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5

    def test_multiply_type_error(self):
        """Test that TypeError is raised for non-numeric inputs."""
        with pytest.raises(TypeError):
            multiply("2", 3)
        with pytest.raises(TypeError):
            multiply(2, "3")


class TestDivide:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(6, 2) == 3

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-6, -2) == 3

    def test_divide_mixed_signs(self):
        """Test dividing with mixed signs."""
        assert divide(6, -2) == -3
        assert divide(-6, 2) == -3

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7.5, 2.5) == 3.0
        assert abs(divide(1, 3) - 0.3333333333) < 1e-9

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        """Test that ValueError is raised when dividing by zero."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            divide(5, 0)

    def test_divide_type_error(self):
        """Test that TypeError is raised for non-numeric inputs."""
        with pytest.raises(TypeError):
            divide("6", 2)
        with pytest.raises(TypeError):
            divide(6, "2")


class TestIntegrationOperations:
    """Integration tests combining multiple operations."""

    def test_chained_operations(self):
        """Test performing multiple operations in sequence."""
        result1 = add(10, 5)  # 15
        result2 = multiply(result1, 2)  # 30
        result3 = divide(result2, 3)  # 10
        assert result3 == 10.0

    def test_complex_calculation(self):
        """Test a complex calculation: (10 + 5) * 2 - 10 / 2."""
        step1 = add(10, 5)  # 15
        step2 = multiply(step1, 2)  # 30
        step3 = divide(10, 2)  # 5
        result = subtract(step2, step3)  # 25
        assert result == 25.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
