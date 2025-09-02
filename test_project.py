#!/usr/bin/env python3
"""
Test suite for project.py calculator
Comprehensive pytest tests covering:
- Basic arithmetic operations
- Scientific functions
- Error handling and edge cases
- Input validation
"""

import pytest
import math
from project import Calculator


class TestCalculator:
    """Test class for Calculator functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    # Test Basic Arithmetic Operations
    
    def test_addition(self):
        """Test addition operation with various inputs."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(1000000, 2000000) == 3000000
    
    def test_subtraction(self):
        """Test subtraction operation with various inputs."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0
        assert self.calc.subtract(0.5, 0.3) == pytest.approx(0.2)
        assert self.calc.subtract(10, 15) == -5
    
    def test_multiplication(self):
        """Test multiplication operation with various inputs."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.multiply(0.5, 4) == 2.0
    
    def test_division(self):
        """Test division operation with various inputs."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3
        assert self.calc.divide(-8, 2) == -4
        assert self.calc.divide(-8, -2) == 4
        assert self.calc.divide(1, 3) == pytest.approx(0.333333, rel=1e-5)
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(-5, 0)
    
    def test_power(self):
        """Test power operation with various inputs."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(-2, 3) == -8
        assert self.calc.power(4, 0.5) == 2.0
    
    def test_power_overflow(self):
        """Test power operation with values that cause overflow."""
        with pytest.raises(ValueError, match="Result too large to compute"):
            self.calc.power(10, 1000)
    
    def test_modulo(self):
        """Test modulo operation with various inputs."""
        assert self.calc.modulo(10, 3) == 1
        assert self.calc.modulo(15, 5) == 0
        assert self.calc.modulo(-10, 3) == 2
        assert self.calc.modulo(10.5, 3) == pytest.approx(1.5)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
            self.calc.modulo(10, 0)
    
    # Test Scientific Functions
    
    def test_square_root(self):
        """Test square root operation."""
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(16) == 4
        assert self.calc.square_root(0) == 0
        assert self.calc.square_root(2) == pytest.approx(1.414213, rel=1e-5)
        assert self.calc.square_root(0.25) == 0.5
    
    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-9)
    
    def test_sine(self):
        """Test sine function."""
        assert self.calc.sine(0) == pytest.approx(0)
        assert self.calc.sine(math.pi/2) == pytest.approx(1)
        assert self.calc.sine(math.pi) == pytest.approx(0, abs=1e-10)
        assert self.calc.sine(-math.pi/2) == pytest.approx(-1)
    
    def test_cosine(self):
        """Test cosine function."""
        assert self.calc.cosine(0) == pytest.approx(1)
        assert self.calc.cosine(math.pi/2) == pytest.approx(0, abs=1e-10)
        assert self.calc.cosine(math.pi) == pytest.approx(-1)
        assert self.calc.cosine(2*math.pi) == pytest.approx(1)
    
    def test_tangent(self):
        """Test tangent function."""
        assert self.calc.tangent(0) == pytest.approx(0)
        assert self.calc.tangent(math.pi/4) == pytest.approx(1)
        assert self.calc.tangent(-math.pi/4) == pytest.approx(-1)
    
    def test_natural_log(self):
        """Test natural logarithm function."""
        assert self.calc.natural_log(math.e) == pytest.approx(1)
        assert self.calc.natural_log(1) == pytest.approx(0)
        assert self.calc.natural_log(math.e**2) == pytest.approx(2)
        assert self.calc.natural_log(0.5) == pytest.approx(-0.693147, rel=1e-5)
    
    def test_natural_log_invalid_input(self):
        """Test natural log with invalid inputs raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.natural_log(0)
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.natural_log(-1)
    
    def test_log_base_10(self):
        """Test base 10 logarithm function."""
        assert self.calc.log_base_10(10) == pytest.approx(1)
        assert self.calc.log_base_10(100) == pytest.approx(2)
        assert self.calc.log_base_10(1) == pytest.approx(0)
        assert self.calc.log_base_10(0.1) == pytest.approx(-1)
    
    def test_log_base_10_invalid_input(self):
        """Test log base 10 with invalid inputs raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.log_base_10(0)
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.log_base_10(-5)
    
    def test_exponential(self):
        """Test exponential function."""
        assert self.calc.exponential(0) == pytest.approx(1)
        assert self.calc.exponential(1) == pytest.approx(math.e)
        assert self.calc.exponential(2) == pytest.approx(math.e**2)
        assert self.calc.exponential(-1) == pytest.approx(1/math.e)
    
    def test_exponential_overflow(self):
        """Test exponential with large values that cause overflow."""
        with pytest.raises(ValueError, match="Result too large to compute"):
            self.calc.exponential(1000)
    
    # Test Angle Conversion Functions
    
    def test_degrees_to_radians(self):
        """Test degrees to radians conversion."""
        assert self.calc.degrees_to_radians(0) == pytest.approx(0)
        assert self.calc.degrees_to_radians(90) == pytest.approx(math.pi/2)
        assert self.calc.degrees_to_radians(180) == pytest.approx(math.pi)
        assert self.calc.degrees_to_radians(360) == pytest.approx(2*math.pi)
        assert self.calc.degrees_to_radians(-90) == pytest.approx(-math.pi/2)
    
    def test_radians_to_degrees(self):
        """Test radians to degrees conversion."""
        assert self.calc.radians_to_degrees(0) == pytest.approx(0)
        assert self.calc.radians_to_degrees(math.pi/2) == pytest.approx(90)
        assert self.calc.radians_to_degrees(math.pi) == pytest.approx(180)
        assert self.calc.radians_to_degrees(2*math.pi) == pytest.approx(360)
        assert self.calc.radians_to_degrees(-math.pi/2) == pytest.approx(-90)
    
    # Test History Functionality
    
    def test_add_to_history(self):
        """Test adding calculations to history."""
        self.calc.add_to_history("2 + 3", 5)
        assert len(self.calc.history) == 1
        assert self.calc.history[0] == "2 + 3 = 5"
        
        self.calc.add_to_history("sqrt(16)", 4)
        assert len(self.calc.history) == 2
        assert self.calc.history[1] == "sqrt(16) = 4"
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add_to_history("2 + 2", 4)
        self.calc.add_to_history("5 * 3", 15)
        assert len(self.calc.history) == 2
        
        self.calc.clear_history()
        assert len(self.calc.history) == 0
    
    # Test Edge Cases and Special Values
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num = 1e10
        assert self.calc.add(large_num, large_num) == 2e10
        assert self.calc.multiply(large_num, 2) == 2e10
    
    def test_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 1e-10
        assert self.calc.add(small_num, small_num) == pytest.approx(2e-10)
        assert self.calc.multiply(small_num, 2) == pytest.approx(2e-10)
    
    def test_floating_point_precision(self):
        """Test floating point precision handling."""
        # Test known floating point precision issues
        result = self.calc.add(0.1, 0.2)
        assert result == pytest.approx(0.3)
        
        result = self.calc.subtract(1.0, 0.9)
        assert result == pytest.approx(0.1)
    
    def test_zero_operations(self):
        """Test operations involving zero."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(100, 0) == 0
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(5, 0) == 1
    
    def test_negative_operations(self):
        """Test operations with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.multiply(-5, -3) == 15
        assert self.calc.divide(-10, -2) == 5
        assert self.calc.power(-2, 3) == -8
        assert self.calc.power(-2, 2) == 4


# Test functions that might be used outside the Calculator class
def test_calculator_instantiation():
    """Test that Calculator can be instantiated properly."""
    calc = Calculator()
    assert calc is not None
    assert hasattr(calc, 'history')
    assert len(calc.history) == 0


if __name__ == "__main__":
    # Run pytest when script is executed directly
    pytest.main(["-v", __file__])
