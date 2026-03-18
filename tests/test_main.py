"""
Integration tests for FastAPI calculator application.
Tests all API endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


class TestRootEndpoint:
    """Test cases for the root endpoint."""

    def test_read_root(self, client):
        """Test GET / returns the HTML template."""
        response = client.get("/")
        assert response.status_code == 200
        assert "FastAPI Calculator" in response.text or "calculator" in response.text.lower()


class TestAddEndpoint:
    """Test cases for the /add endpoint."""

    def test_add_valid_numbers(self, client):
        """Test adding two valid numbers."""
        response = client.post("/add", json={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_add_negative_numbers(self, client):
        """Test adding negative numbers."""
        response = client.post("/add", json={"a": -5, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_add_floats(self, client):
        """Test adding floating point numbers."""
        response = client.post("/add", json={"a": 2.5, "b": 3.5})
        assert response.status_code == 200
        assert response.json() == {"result": 6.0}

    def test_add_missing_field(self, client):
        """Test add endpoint with missing field."""
        response = client.post("/add", json={"a": 2})
        assert response.status_code == 422  # Validation error

    def test_add_invalid_type(self, client):
        """Test add endpoint with invalid type."""
        response = client.post("/add", json={"a": "two", "b": 3})
        assert response.status_code == 422  # Validation error


class TestSubtractEndpoint:
    """Test cases for the /subtract endpoint."""

    def test_subtract_valid_numbers(self, client):
        """Test subtracting two valid numbers."""
        response = client.post("/subtract", json={"a": 5, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_subtract_negative_result(self, client):
        """Test subtraction resulting in negative number."""
        response = client.post("/subtract", json={"a": 3, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_subtract_floats(self, client):
        """Test subtracting floating point numbers."""
        response = client.post("/subtract", json={"a": 5.5, "b": 2.5})
        assert response.status_code == 200
        assert response.json() == {"result": 3.0}

    def test_subtract_from_zero(self, client):
        """Test subtracting from zero."""
        response = client.post("/subtract", json={"a": 0, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": -5}


class TestMultiplyEndpoint:
    """Test cases for the /multiply endpoint."""

    def test_multiply_valid_numbers(self, client):
        """Test multiplying two valid numbers."""
        response = client.post("/multiply", json={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 6}

    def test_multiply_by_zero(self, client):
        """Test multiplying by zero."""
        response = client.post("/multiply", json={"a": 5, "b": 0})
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_multiply_negative_numbers(self, client):
        """Test multiplying negative numbers."""
        response = client.post("/multiply", json={"a": -2, "b": -3})
        assert response.status_code == 200
        assert response.json() == {"result": 6}

    def test_multiply_mixed_signs(self, client):
        """Test multiplying with mixed signs."""
        response = client.post("/multiply", json={"a": 2, "b": -3})
        assert response.status_code == 200
        assert response.json() == {"result": -6}

    def test_multiply_floats(self, client):
        """Test multiplying floating point numbers."""
        response = client.post("/multiply", json={"a": 2.5, "b": 4})
        assert response.status_code == 200
        assert response.json() == {"result": 10.0}


class TestDivideEndpoint:
    """Test cases for the /divide endpoint."""

    def test_divide_valid_numbers(self, client):
        """Test dividing two valid numbers."""
        response = client.post("/divide", json={"a": 6, "b": 2})
        assert response.status_code == 200
        assert response.json() == {"result": 3}

    def test_divide_floats(self, client):
        """Test dividing floating point numbers."""
        response = client.post("/divide", json={"a": 7.5, "b": 2.5})
        assert response.status_code == 200
        assert response.json() == {"result": 3.0}

    def test_divide_by_zero(self, client):
        """Test that dividing by zero returns error."""
        response = client.post("/divide", json={"a": 5, "b": 0})
        assert response.status_code == 400
        assert "Division by zero" in response.json()["error"]

    def test_divide_zero_by_number(self, client):
        """Test dividing zero by a number."""
        response = client.post("/divide", json={"a": 0, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_divide_negative_numbers(self, client):
        """Test dividing negative numbers."""
        response = client.post("/divide", json={"a": -6, "b": -2})
        assert response.status_code == 200
        assert response.json() == {"result": 3}

    def test_divide_mixed_signs(self, client):
        """Test dividing with mixed signs."""
        response = client.post("/divide", json={"a": 6, "b": -2})
        assert response.status_code == 200
        assert response.json() == {"result": -3}


class TestErrorHandling:
    """Test error handling for invalid requests."""

    def test_invalid_request_format(self, client):
        """Test request with invalid JSON format."""
        response = client.post("/add", json={"invalid": "data"})
        assert response.status_code == 422

    def test_empty_request(self, client):
        """Test request with empty body."""
        response = client.post("/add", json={})
        assert response.status_code == 422

    def test_null_values(self, client):
        """Test request with null values."""
        response = client.post("/add", json={"a": None, "b": 3})
        assert response.status_code == 422


class TestIntegrationScenarios:
    """Integration tests with multiple endpoint calls."""

    def test_calculator_workflow(self, client):
        """Test a complete calculator workflow."""
        # Add
        response = client.post("/add", json={"a": 10, "b": 5})
        assert response.status_code == 200
        result_add = response.json()["result"]  # 15

        # Multiply
        response = client.post("/multiply", json={"a": result_add, "b": 2})
        assert response.status_code == 200
        result_multiply = response.json()["result"]  # 30

        # Divide
        response = client.post("/divide", json={"a": result_multiply, "b": 3})
        assert response.status_code == 200
        result_divide = response.json()["result"]  # 10

        assert result_divide == 10.0

    def test_error_recovery(self, client):
        """Test that API recovers after an error."""
        # Send an error request
        response = client.post("/divide", json={"a": 5, "b": 0})
        assert response.status_code == 400

        # Verify next request works fine
        response = client.post("/add", json={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 5}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
