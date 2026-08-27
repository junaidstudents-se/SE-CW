# Lab 01 — Enhanced Python Calculator

## Overview

This is an enhanced version of the Python Calculator lab project for Software Engineering. It demonstrates fundamental programming concepts including functions with type hints, user input handling, conditional statements, exception handling, and comprehensive software testing.

## Course Information

- **Course**: Software Engineering
- **Lab Title**: Introduction to Python, Git, GitHub, and Testing
- **Duration**: 2-3 Hours
- **Difficulty**: Beginner to Intermediate

---

## Learning Objectives

After completing this lab, students will be able to:

1. ✓ Create and execute Python programs with proper structure
2. ✓ Define and use functions with type hints
3. ✓ Implement conditional statements and loops
4. ✓ Handle user input with validation
5. ✓ Implement comprehensive exception handling
6. ✓ Use Git for version control
7. ✓ Create meaningful commits and branches
8. ✓ Push code to GitHub and create pull requests
9. ✓ Write automated tests using pytest
10. ✓ Execute and verify tests with proper coverage
11. ✓ Implement code linting and formatting standards
12. ✓ Use type checking and static analysis

---

## Features

### Core Operations (8 Functions)

| Operation | Input | Description |
|-----------|-------|-------------|
| **Addition** | 2 numbers | Returns sum of two numbers |
| **Subtraction** | 2 numbers | Returns difference between numbers |
| **Multiplication** | 2 numbers | Returns product of two numbers |
| **Division** | 2 numbers | Returns quotient (handles zero division) |
| **Modulus** | 2 numbers | Returns remainder of division |
| **Power** | 2 numbers | Raises base to exponent power |
| **Square Root** | 1 number | Returns square root (no negatives) |
| **Factorial** | 1 number | Returns factorial (non-negative integers only) |

### Code Quality Features

- ✓ **Type Hints**: Full type annotations for all functions
- ✓ **Docstrings**: Comprehensive documentation for every function
- ✓ **Exception Handling**: Proper error handling with meaningful messages
- ✓ **Input Validation**: Robust validation for user inputs
- ✓ **Code Formatting**: Black code formatter compatibility
- ✓ **Linting**: Flake8 compliant code style

---

## Software Requirements

### Required Tools

- **Python 3.8+** (tested on 3.8, 3.9, 3.10, 3.11)
- **Git** (for version control)
- **GitHub account** (for repository hosting)

### Recommended Tools

- **VS Code** or **PyCharm** IDE
- **pip** (Python package manager)

### Alternative

- **Google Colab** (cloud-based Python environment)

---

## Project Structure

```
SE-CW/
├── .github/
│   └── workflows/
│       └── calculator-tests.yml      # GitHub Actions CI/CD workflow
├── .flake8                           # Flake8 linting configuration
├── .gitignore                        # Git ignore rules
├── pyproject.toml                    # Project configuration (pytest, black, mypy)
├── README.md                         # Main project documentation
│
└── SELab1/
    ├── calculator.py                 # Main calculator module with 8 operations
    ├── test_calculator.py            # Comprehensive test suite (50+ tests)
    ├── demo.py                       # Demonstration script
    ├── requirements.txt              # Python dependencies
    ├── README.md                     # Lab-specific documentation
    └── student-task.md               # Student assignment tasks
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/junaidstudents-se/SE-CW.git
cd SE-CW
```

### 2. Switch to SELab3 Branch

```bash
git checkout SELab3
```

### 3. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r SELab1/requirements.txt
```

---

## Usage

### Interactive Calculator

Run the calculator in interactive mode:

```bash
cd SELab1
python calculator.py
```

**Example Session:**
```
===================================
       ENHANCED SIMPLE CALCULATOR
    Software Engineering Lab 01
===================================

Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Square Root
8. Factorial
9. Exit

Enter your choice (1-9): 1
Enter first number: 10
Enter second number: 5

Result: 15
```

### Run Demonstration Script

View all operations in action:

```bash
cd SELab1
python demo.py
```

### Run All Tests

Execute the comprehensive test suite:

```bash
cd SELab1
pytest test_calculator.py -v
```

### Run Tests with Coverage Report

Generate code coverage analysis:

```bash
cd SELab1
pytest test_calculator.py -v --cov=. --cov-report=html
```

### Code Quality Checks

#### Linting with Flake8
```bash
cd SELab1
flake8 calculator.py --max-line-length=100
```

#### Format Check with Black
```bash
cd SELab1
black --check calculator.py test_calculator.py
```

#### Type Checking with MyPy
```bash
cd SELab1
mypy calculator.py --strict
```

---

## Test Coverage

### Test Statistics

- **Total Tests**: 50+
- **Test Classes**: 9
- **Test Categories**: Addition, Subtraction, Multiplication, Division, Modulus, Power, Square Root, Factorial, Integration
- **Coverage Target**: >95% code coverage

### Test Categories

| Category | Tests | Coverage |
|----------|-------|----------|
| Addition | 6 | Positive, negative, decimals, zero, large numbers |
| Subtraction | 6 | Positive, negative, decimals, zero, same number |
| Multiplication | 6 | Positive, negative, decimals, zero, one, large numbers |
| Division | 6 | Positive, negative, zero handling, decimals |
| Modulus | 6 | Positive, negative, decimals, equal numbers, zero |
| Power | 7 | Positive/negative, zero exp, fractional, base zero |
| Square Root | 7 | Perfect squares, decimals, negatives, non-perfect |
| Factorial | 5 | Small/large integers, floats, negatives, decimals |
| Integration | 4 | Combined multi-operation tests |

### Example Test Run

```
collected 50 items

SELab1/test_calculator.py::TestAddition::test_add_positive_integers PASSED
SELab1/test_calculator.py::TestAddition::test_add_negative_integers PASSED
SELab1/test_calculator.py::TestAddition::test_add_mixed_signs PASSED
...
======================== 50 passed in 0.45s ========================
```

---

## Key Improvements Made

### 1. **Enhanced Calculator Functions**
- Added Modulus operation (%)
- Added Power operation (**)
- Added Square Root operation (math.sqrt)
- Added Factorial operation (math.factorial)

### 2. **Type Hints**
- Full type annotations for all functions
- Return type documentation
- Parameter type specifications

### 3. **Comprehensive Testing**
- 50+ test cases covering all operations
- Edge case testing (negative numbers, decimals, boundaries)
- Exception handling verification
- Integration tests combining operations

### 4. **Code Quality Standards**
- Black code formatter configuration
- Flake8 linting setup
- MyPy static type checking
- Configurable via pyproject.toml

### 5. **Project Organization**
- Added .gitignore for Python projects
- Professional directory structure
- Configuration files (pyproject.toml, .flake8)
- Demonstration script

### 6. **CI/CD Pipeline**
- GitHub Actions workflow for automated testing
- Multi-version Python testing (3.8, 3.9, 3.10, 3.11)
- Automated linting and type checking
- Coverage report generation

---

## Student Tasks

### Task 1: Run the Calculator
Execute the calculator and test all operations:
- Addition, Subtraction, Multiplication, Division
- Modulus and Power operations
- Square Root and Factorial
- Test error handling (division by zero, negative square root)

### Task 2: Understand the Code
Identify the following in `calculator.py`:
1. Function definitions with type hints
2. Conditional statements (if/elif/else)
3. Loop structures (while)
4. Exception handling (try/except)
5. User input operations
6. Program entry point (if __name__ == "__main__")

### Task 3: Run Tests
Execute all tests and verify:
```bash
pytest test_calculator.py -v --cov=.
```

Ensure all 50+ tests pass with high coverage.

### Task 4: Code Quality Checks
Run all quality tools:
```bash
flake8 calculator.py
black --check calculator.py test_calculator.py
mypy calculator.py --strict
```

### Task 5: Git Exercise
Create a branch and commit changes:
```bash
git checkout -b student-name-lab01
git add SELab1/
git commit -m "Complete enhanced calculator implementation"
git push origin student-name-lab01
```

### Task 6: Documentation
Create `answers.md` containing:
- Student name and registration number
- Explanation of the program architecture
- Summary of all operations implemented
- Test coverage analysis
- Key learnings and improvements made

---

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Ensure you're in the correct directory and requirements are installed
```bash
cd SELab1
pip install -r requirements.txt
```

### Issue: Factorial Error for Whole Numbers
**Solution**: The factorial function now properly handles float inputs that are whole numbers (e.g., 5.0)

### Issue: Tests Fail
**Solution**: Verify Python version and dependencies:
```bash
python --version  # Should be 3.8+
pip install -r requirements.txt --upgrade
pytest test_calculator.py -v
```

### Issue: Linting Warnings
**Solution**: Format code with Black:
```bash
cd SELab1
black calculator.py test_calculator.py
```

---

## GitHub Workflow

### Local Development

```bash
# 1. Create feature branch
git checkout -b feature/new-operation

# 2. Make changes and test
python calculator.py
pytest test_calculator.py -v

# 3. Verify code quality
flake8 calculator.py
black calculator.py

# 4. Commit with meaningful message
git add .
git commit -m "Add new operation with comprehensive tests"

# 5. Push to GitHub
git push origin feature/new-operation

# 6. Create Pull Request on GitHub
```

### Automated Checks

The GitHub Actions workflow automatically:
- ✓ Runs tests on Python 3.8, 3.9, 3.10, 3.11
- ✓ Generates coverage reports
- ✓ Performs flake8 linting
- ✓ Checks code formatting with Black
- ✓ Runs MyPy type checking
- ✓ Uploads coverage to Codecov

---

## Resources

### Python Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Math Module](https://docs.python.org/3/library/math.html)

### Testing
- [pytest Documentation](https://docs.pytest.org/)
- [pytest Coverage](https://pytest-cov.readthedocs.io/)

### Code Quality
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [MyPy Type Checker](https://www.mypy-lang.org/)

### Git & GitHub
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## Submission

Submit your work via:

1. **GitHub Repository URL** (SELab3 branch)
2. **Pull Request** linking to main branch
3. **Completed answers.md** with documentation

---

## License

This project is part of the Software Engineering course curriculum.

---

## Contact & Support

For questions or issues:
- Review the troubleshooting section
- Check existing GitHub issues
- Contact course instructor

**Last Updated**: August 2026
**Version**: 2.0 (Enhanced with 8 operations, comprehensive tests, and CI/CD)
