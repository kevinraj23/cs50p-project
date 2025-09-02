# Advanced Python Calculator

## YouTube Demo
Coming soon

## Project Description

The Advanced Python Calculator is a comprehensive, command-line calculator application developed as a CS50P final project. This project demonstrates advanced Python programming concepts including object-oriented programming, error handling, mathematical computations, and comprehensive testing methodologies.

### Overview

This calculator goes far beyond basic arithmetic operations, offering a sophisticated scientific computing environment through an intuitive interactive menu system. The application is built around a robust Calculator class that encapsulates all mathematical operations and maintains calculation history, showcasing proper software engineering principles.

### Key Features

**Basic Arithmetic Operations:**
- Addition, subtraction, multiplication, and division
- Exponentiation (power operations)
- Modulo operations with comprehensive error handling

**Scientific Functions:**
- Trigonometric functions (sine, cosine, tangent) with radian input
- Logarithmic functions (natural log and base-10 logarithm)
- Square root calculations with negative number validation
- Exponential functions (e^x) with overflow protection
- Angle conversion utilities (degrees ↔ radians)

**Advanced Features:**
- Interactive calculation history tracking (stores last 10 calculations)
- Robust error handling for all edge cases (division by zero, negative square roots, logarithm domain errors)
- Graceful handling of numerical overflow conditions
- User-friendly menu-driven interface with quit functionality
- Floating-point precision arithmetic throughout

### Original Aspects and Design Philosophy

This calculator distinguishes itself from basic calculator templates through several innovative design choices:

1. **Object-Oriented Architecture**: The Calculator class encapsulates state and behavior, enabling features like persistent history tracking and modular function organization.

2. **Comprehensive Error Handling**: Every mathematical operation includes domain validation and overflow protection, providing informative error messages rather than cryptic exceptions.

3. **Interactive User Experience**: The menu-driven interface allows users to perform multiple calculations in a session, with the ability to review calculation history and clear it as needed.

4. **Scientific Computing Focus**: Beyond basic arithmetic, the calculator provides trigonometric and logarithmic functions essential for scientific and engineering applications.

### Mathematical and Scientific Details

The calculator leverages Python's `math` module for precision scientific computations:
- Trigonometric functions operate in radians (the mathematical standard) with conversion utilities provided
- Logarithmic functions include both natural logarithm (ln) and common logarithm (log₁₀)
- Square root operations use the optimized `math.sqrt()` implementation
- Exponential functions utilize `math.exp()` for e^x calculations
- All operations maintain IEEE 754 floating-point precision

### Usage Instructions

To run the calculator:
```bash
python project.py
```

The application presents an interactive menu with 18 options:
- Options 1-6: Basic arithmetic operations
- Options 7-13: Scientific functions
- Options 14-15: Angle conversions
- Options 16-17: History management
- Option 18: Exit application

Users can quit any operation by entering 'q', and the application handles keyboard interrupts gracefully.

### Testing and Quality Assurance

The project includes a comprehensive pytest test suite (`test_project.py`) that validates:
- All basic arithmetic operations with various input types
- Scientific function accuracy and domain validation
- Error handling for edge cases (division by zero, negative inputs for logs/square roots)
- History management functionality
- Input validation and error recovery

### How to Run and Test

1. **Installation**: Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Running the Calculator**:
   ```bash
   python project.py
   ```

3. **Running Tests**:
   ```bash
   pytest test_project.py -v
   ```

### Project Motivation

This project was developed to demonstrate mastery of Python programming fundamentals while creating a genuinely useful tool. The motivation was to build something more substantial than a basic four-function calculator—a scientific computing tool that showcases:

- Advanced error handling and input validation
- Object-oriented design principles
- Mathematical computing with proper precision
- Comprehensive testing methodologies
- User experience design in command-line applications

The calculator serves as both a practical tool for mathematical computations and a demonstration of software engineering best practices in Python development. Every aspect of the code, from the class architecture to the error messages, was designed with user experience and code maintainability in mind.

This project represents original work that goes significantly beyond copying existing calculator templates, incorporating advanced features like scientific functions, calculation history, robust error handling, and a comprehensive test suite that validates both functionality and edge cases.
