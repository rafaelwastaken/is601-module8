"""
End-to-End tests for FastAPI Calculator application.
Tests user interactions using Playwright.
"""

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def browser_context():
    """Create a browser context for testing."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        yield context
        browser.close()


@pytest.fixture
def page(browser_context):
    """Create a page for testing."""
    return browser_context.new_page()


class TestCalculatorUI:
    """Test cases for calculator UI interactions."""

    def test_page_loads(self, page):
        """Test that the calculator page loads successfully."""
        page.goto("http://localhost:8000")
        expect(page).to_have_title("FastAPI Calculator")
        
        # Check for main heading
        heading = page.locator("h1")
        expect(heading).to_contain_text("Calculator")

    def test_input_fields_exist(self, page):
        """Test that input fields are present on the page."""
        page.goto("http://localhost:8000")
        
        # Check for number inputs
        input1 = page.locator("#num1")
        input2 = page.locator("#num2")
        
        expect(input1).to_be_visible()
        expect(input2).to_be_visible()

    def test_operation_buttons_exist(self, page):
        """Test that all operation buttons are present."""
        page.goto("http://localhost:8000")
        
        buttons = page.locator("button")
        expect(buttons).to_have_count(4)  # Add, Subtract, Multiply, Divide

    def test_add_operation(self, page):
        """Test adding two numbers via UI."""
        page.goto("http://localhost:8000")
        
        # Fill in inputs
        page.fill("#num1", "10")
        page.fill("#num2", "5")
        
        # Click add button
        page.click("button:has-text('Add')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("15")

    def test_subtract_operation(self, page):
        """Test subtracting two numbers via UI."""
        page.goto("http://localhost:8000")
        
        # Fill in inputs
        page.fill("#num1", "10")
        page.fill("#num2", "3")
        
        # Click subtract button
        page.click("button:has-text('Subtract')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("7")

    def test_multiply_operation(self, page):
        """Test multiplying two numbers via UI."""
        page.goto("http://localhost:8000")
        
        # Fill in inputs
        page.fill("#num1", "4")
        page.fill("#num2", "5")
        
        # Click multiply button
        page.click("button:has-text('Multiply')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("20")

    def test_divide_operation(self, page):
        """Test dividing two numbers via UI."""
        page.goto("http://localhost:8000")
        
        # Fill in inputs
        page.fill("#num1", "20")
        page.fill("#num2", "4")
        
        # Click divide button
        page.click("button:has-text('Divide')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("5")

    def test_negative_numbers(self, page):
        """Test operations with negative numbers."""
        page.goto("http://localhost:8000")
        
        # Fill in negative numbers
        page.fill("#num1", "-10")
        page.fill("#num2", "5")
        
        # Click add button
        page.click("button:has-text('Add')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("-5")

    def test_decimal_numbers(self, page):
        """Test operations with decimal numbers."""
        page.goto("http://localhost:8000")
        
        # Fill in decimal numbers
        page.fill("#num1", "7.5")
        page.fill("#num2", "2.5")
        
        # Click divide button
        page.click("button:has-text('Divide')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("3")

    def test_division_by_zero_error(self, page):
        """Test that division by zero shows an error."""
        page.goto("http://localhost:8000")
        
        # Fill in numbers with zero divisor
        page.fill("#num1", "10")
        page.fill("#num2", "0")
        
        # Click divide button
        page.click("button:has-text('Divide')")
        
        # Wait for error message
        result = page.locator("#result-value")
        expect(result).to_contain_text("not allowed", ignore_case=True)

    def test_invalid_input_error(self, page):
        """Test that invalid input shows an error."""
        page.goto("http://localhost:8000")
        
        # Click add without filling inputs
        page.click("button:has-text('Add')")
        
        # Check for error message
        result = page.locator("#result-value")
        expect(result).to_contain_text("valid numbers")

    def test_multiple_consecutive_operations(self, page):
        """Test performing multiple operations in sequence."""
        page.goto("http://localhost:8000")
        
        # First operation: 5 + 3 = 8
        page.fill("#num1", "5")
        page.fill("#num2", "3")
        page.click("button:has-text('Add')")
        result = page.locator("#result-value")
        expect(result).to_contain_text("8")
        
        # Second operation: 10 - 4 = 6
        page.fill("#num1", "10")
        page.fill("#num2", "4")
        page.click("button:has-text('Subtract')")
        expect(result).to_contain_text("6")
        
        # Third operation: 2 * 9 = 18
        page.fill("#num1", "2")
        page.fill("#num2", "9")
        page.click("button:has-text('Multiply')")
        expect(result).to_contain_text("18")

    def test_clearing_inputs(self, page):
        """Test that inputs can be cleared and used again."""
        page.goto("http://localhost:8000")
        
        # Fill and compute
        page.fill("#num1", "10")
        page.fill("#num2", "2")
        page.click("button:has-text('Divide')")
        result = page.locator("#result-value")
        expect(result).to_contain_text("5")
        
        # Clear and perform new operation
        page.fill("#num1", "100")
        page.fill("#num2", "10")
        page.click("button:has-text('Divide')")
        expect(result).to_contain_text("10")

    def test_large_numbers(self, page):
        """Test operations with large numbers."""
        page.goto("http://localhost:8000")
        
        # Fill in large numbers
        page.fill("#num1", "1000000")
        page.fill("#num2", "500000")
        
        # Click add button
        page.click("button:has-text('Add')")
        
        # Wait for result
        result = page.locator("#result-value")
        expect(result).to_contain_text("1500000")

    def test_zero_operations(self, page):
        """Test operations involving zero."""
        page.goto("http://localhost:8000")
        
        # 0 + 5 = 5
        page.fill("#num1", "0")
        page.fill("#num2", "5")
        page.click("button:has-text('Add')")
        result = page.locator("#result-value")
        expect(result).to_contain_text("5")
        
        # 5 * 0 = 0
        page.fill("#num1", "5")
        page.fill("#num2", "0")
        page.click("button:has-text('Multiply')")
        expect(result).to_have_text("0")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
