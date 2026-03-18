"""
Calculator operations module.
Provides basic arithmetic operations: add, subtract, multiply, and divide.
"""

import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a (float): The first number
        b (float): The second number
    
    Returns:
        float: The sum of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    logger.info(f"Adding {a} + {b}")
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.
    
    Args:
        a (float): The first number
        b (float): The second number
    
    Returns:
        float: The difference of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    logger.info(f"Subtracting {a} - {b}")
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a (float): The first number
        b (float): The second number
    
    Returns:
        float: The product of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    logger.info(f"Multiplying {a} * {b}")
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Args:
        a (float): The dividend (numerator)
        b (float): The divisor (denominator)
    
    Returns:
        float: The quotient of a divided by b
    
    Raises:
        TypeError: If either argument is not a number
        ValueError: If attempting to divide by zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        logger.error(f"Division by zero attempted: {a} / {b}")
        raise ValueError("Division by zero is not allowed")
    logger.info(f"Dividing {a} / {b}")
    return a / b
