#!/usr/bin/env python3
"""
Advanced Python Calculator

A comprehensive calculator supporting:
- Basic arithmetic operations (+, -, *, /, **, %)
- Scientific functions (sin, cos, tan, log, log10, sqrt, exp)
- Floating-point math with robust error handling
- Interactive CLI menu interface

Author: CS50P Project
Date: September 2025
"""

import math
import sys


class Calculator:
    """Advanced calculator class with scientific functions and error handling."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []  # Store calculation history
    
    def add(self, x, y):
        """Addition operation."""
        return x + y
    
    def subtract(self, x, y):
        """Subtraction operation."""
        return x - y
    
    def multiply(self, x, y):
        """Multiplication operation."""
        return x * y
    
    def divide(self, x, y):
        """Division operation with zero division handling."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def power(self, x, y):
        """Power operation (x^y)."""
        try:
            return x ** y
        except OverflowError:
            raise ValueError("Result too large to compute")
    
    def modulo(self, x, y):
        """Modulo operation with zero division handling."""
        if y == 0:
            raise ValueError("Cannot perform modulo with zero")
        return x % y
    
    def square_root(self, x):
        """Square root operation."""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    def sine(self, x):
        """Sine function (input in radians)."""
        return math.sin(x)
    
    def cosine(self, x):
        """Cosine function (input in radians)."""
        return math.cos(x)
    
    def tangent(self, x):
        """Tangent function (input in radians)."""
        return math.tan(x)
    
    def natural_log(self, x):
        """Natural logarithm (base e)."""
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log(x)
    
    def log_base_10(self, x):
        """Logarithm base 10."""
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log10(x)
    
    def exponential(self, x):
        """Exponential function (e^x)."""
        try:
            return math.exp(x)
        except OverflowError:
            raise ValueError("Result too large to compute")
    
    def degrees_to_radians(self, degrees):
        """Convert degrees to radians."""
        return math.radians(degrees)
    
    def radians_to_degrees(self, radians):
        """Convert radians to degrees."""
        return math.degrees(radians)
    
    def add_to_history(self, operation, result):
        """Add calculation to history."""
        self.history.append(f"{operation} = {result}")
    
    def show_history(self):
        """Display calculation history."""
        if not self.history:
            print("No calculations in history.")
            return
        
        print("\n=== Calculation History ===")
        for i, calc in enumerate(self.history[-10:], 1):  # Show last 10
            print(f"{i}. {calc}")
        print()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
        print("History cleared.")


def get_number(prompt):
    """Get a valid number from user input with error handling."""
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'q':
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")


def get_two_numbers():
    """Get two numbers from user input."""
    x = get_number("Enter first number (or 'q' to quit): ")
    if x is None:
        return None, None
    
    y = get_number("Enter second number (or 'q' to quit): ")
    if y is None:
        return None, None
    
    return x, y


def get_one_number():
    """Get one number from user input."""
    return get_number("Enter number (or 'q' to quit): ")


def display_menu():
    """Display the main calculator menu."""
    print("\n" + "="*50)
    print("       ADVANCED PYTHON CALCULATOR")
    print("="*50)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (**)")
    print("  6. Modulo (%)")
    print("\nScientific Functions:")
    print("  7. Square Root")
    print("  8. Sine (radians)")
    print("  9. Cosine (radians)")
    print(" 10. Tangent (radians)")
    print(" 11. Natural Logarithm (ln)")
    print(" 12. Logarithm Base 10")
    print(" 13. Exponential (e^x)")
    print("\nAngle Conversion:")
    print(" 14. Degrees to Radians")
    print(" 15. Radians to Degrees")
    print("\nUtilities:")
    print(" 16. Show History")
    print(" 17. Clear History")
    print(" 18. Quit")
    print("="*50)


def main():
    """Main calculator function with interactive menu."""
    calc = Calculator()
    
    print("Welcome to the Advanced Python Calculator!")
    print("This calculator supports floating-point arithmetic and scientific functions.")
    print("You can quit any operation by entering 'q'.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nSelect an operation (1-18): ").strip()
            
            if choice == '18' or choice.lower() == 'q':
                print("Thank you for using the Advanced Python Calculator!")
                sys.exit(0)
            
            elif choice == '1':  # Addition
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.add(x, y)
                operation = f"{x} + {y}"
                
            elif choice == '2':  # Subtraction
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.subtract(x, y)
                operation = f"{x} - {y}"
                
            elif choice == '3':  # Multiplication
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.multiply(x, y)
                operation = f"{x} * {y}"
                
            elif choice == '4':  # Division
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.divide(x, y)
                operation = f"{x} / {y}"
                
            elif choice == '5':  # Power
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.power(x, y)
                operation = f"{x} ** {y}"
                
            elif choice == '6':  # Modulo
                x, y = get_two_numbers()
                if x is None or y is None:
                    continue
                result = calc.modulo(x, y)
                operation = f"{x} % {y}"
                
            elif choice == '7':  # Square Root
                x = get_one_number()
                if x is None:
                    continue
                result = calc.square_root(x)
                operation = f"sqrt({x})"
                
            elif choice == '8':  # Sine
                x = get_one_number()
                if x is None:
                    continue
                result = calc.sine(x)
                operation = f"sin({x})"
                
            elif choice == '9':  # Cosine
                x = get_one_number()
                if x is None:
                    continue
                result = calc.cosine(x)
                operation = f"cos({x})"
                
            elif choice == '10':  # Tangent
                x = get_one_number()
                if x is None:
                    continue
                result = calc.tangent(x)
                operation = f"tan({x})"
                
            elif choice == '11':  # Natural Log
                x = get_one_number()
                if x is None:
                    continue
                result = calc.natural_log(x)
                operation = f"ln({x})"
                
            elif choice == '12':  # Log Base 10
                x = get_one_number()
                if x is None:
                    continue
                result = calc.log_base_10(x)
                operation = f"log10({x})"
                
            elif choice == '13':  # Exponential
                x = get_one_number()
                if x is None:
                    continue
                result = calc.exponential(x)
                operation = f"exp({x})"
                
            elif choice == '14':  # Degrees to Radians
                x = get_one_number()
                if x is None:
                    continue
                result = calc.degrees_to_radians(x)
                operation = f"{x}° to radians"
                
            elif choice == '15':  # Radians to Degrees
                x = get_one_number()
                if x is None:
                    continue
                result = calc.radians_to_degrees(x)
                operation = f"{x} radians to degrees"
                
            elif choice == '16':  # Show History
                calc.show_history()
                input("Press Enter to continue...")
                continue
                
            elif choice == '17':  # Clear History
                calc.clear_history()
                input("Press Enter to continue...")
                continue
                
            else:
                print("Invalid choice. Please select a number from 1-18.")
                input("Press Enter to continue...")
                continue
            
            # Display result and add to history
            print(f"\nResult: {result}")
            calc.add_to_history(operation, result)
            input("Press Enter to continue...")
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
