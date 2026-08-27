# DEVELOPMENT GUIDE
## SELab1 Enhanced Calculator - Developer Workflow

**Purpose**: This guide provides step-by-step instructions for developers to work with the Enhanced Calculator project, including setup, development, testing, and deployment.

**Target Audience**: Students, developers, and contributors

---

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Development Workflow](#development-workflow)
3. [Testing Guidelines](#testing-guidelines)
4. [Code Quality Standards](#code-quality-standards)
5. [Debugging Tips](#debugging-tips)
6. [Common Tasks](#common-tasks)
7. [Troubleshooting](#troubleshooting)

---

## Environment Setup

### Prerequisites

- Python 3.8 or higher
- Git installed
- GitHub account
- Code editor (VS Code, PyCharm, etc.)
- Terminal/Command Prompt access

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/junaidstudents-se/SE-CW.git

# Navigate to project directory
cd SE-CW
```

### Step 2: Switch to Development Branch

```bash
# Check available branches
git branch -a

# Switch to SELab3 branch
git checkout SELab3

# Verify current branch
git branch
```

### Step 3: Create Virtual Environment

#### On Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify activation (should see (venv) in prompt)
```

#### On macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (should see (venv) in prompt)
```

### Step 4: Install Dependencies

```bash
# Ensure you're in project root directory
cd SE-CW

# Install all required packages
pip install -r SELab1/requirements.txt

# Verify installation
pip list
```

### Step 5: Verify Setup

```bash
# Navigate to lab directory
cd SELab1

# Run the demo script
python demo.py

# Expected output: All operations displayed with results
```

---

## Development Workflow

### 1. Creating a Feature Branch

```bash
# Update main branch first
git checkout main
git pull origin main

# Create new feature branch
git checkout -b feature/your-feature-name

# Naming conventions:
# - feature/new-operation
# - bugfix/factorial-issue
# - enhancement/better-error-messages
# - docs/update-readme
```

### 2. Making Changes

```bash
# Edit files in SELab1/ directory
# Example: SELab1/calculator.py

# Verify changes work
cd SELab1
python calculator.py

# Run tests to ensure nothing broke
pytest test_calculator.py -v
```

### 3. Committing Changes

```bash
# Check what changed
git status

# Add specific files
git add SELab1/calculator.py
git add SELab1/test_calculator.py

# Or add all changes
git add .

# Create meaningful commit message
git commit -m "Add new operation or fix with brief description"

# Commit message format:
# [Type]: [Brief description]
# - feature: Add new functionality
# - bugfix: Fix existing issue
# - enhancement: Improve existing code
# - docs: Update documentation
# - test: Add or update tests

# Examples:
# git commit -m "feature: Add new Square Root operation"
# git commit -m "bugfix: Fix factorial handling for float inputs"
# git commit -m "test: Add comprehensive edge case tests"
```

### 4. Pushing to GitHub

```bash
# Push branch to GitHub
git push origin feature/your-feature-name

# Or set upstream and push
git push -u origin feature/your-feature-name

# Verify push was successful
git log --oneline -5
```

### 5. Creating Pull Request

1. Go to: https://github.com/junaidstudents-se/SE-CW
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select:
   - Base branch: `SELab3`
   - Compare branch: `feature/your-feature-name`
5. Add title and description
6. Click "Create pull request"

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Enhancement
- [ ] Documentation

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Code coverage >95%

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests pass locally
- [ ] No new warnings
```

---

## Testing Guidelines

### Running Tests

#### Run All Tests
```bash
cd SELab1
pytest test_calculator.py -v
```

#### Run Specific Test Class
```bash
pytest test_calculator.py::TestAddition -v
```

#### Run Specific Test Method
```bash
pytest test_calculator.py::TestAddition::test_add_positive_integers -v
```

#### Run Tests Matching Pattern
```bash
# Run all tests with "factorial" in name
pytest test_calculator.py -k factorial -v
```

#### Run with Coverage Report
```bash
# Generate coverage report
pytest test_calculator.py -v --cov=. --cov-report=html

# View HTML report
# Open htmlcov/index.html in browser
```

### Writing New Tests

#### Test Structure

```python
class TestNewOperation:
    """Test cases for new operation."""
    
    def test_basic_functionality(self):
        """Test basic case."""
        result = new_operation(10, 5)
        assert result == expected_value
    
    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError, match="Error message"):
            new_operation(invalid_input)
    
    def test_edge_case(self):
        """Test edge case."""
        result = new_operation(0, 5)
        assert result == expected_value
```

#### Using pytest Assertions

```python
# Basic assertions
assert result == expected
assert result > 0
assert result < 100

# Approximate equality (for floats)
import pytest
assert result == pytest.approx(3.14)

# Exception testing
with pytest.raises(ValueError):
    function_that_raises()

# Exception message checking
with pytest.raises(ValueError, match="error text"):
    function_that_raises()
```

#### Test Naming Conventions

```python
# Format: test_<function>_<scenario>
def test_add_positive_integers():
    """Test adding positive integers."""

def test_divide_by_zero_raises_error():
    """Test that dividing by zero raises ValueError."""

def test_factorial_float_whole_numbers():
    """Test factorial with float that are whole numbers."""

def test_square_root_negative_raises_error():
    """Test that negative square root raises ValueError."""
```

### Test Coverage Goals

- **Minimum**: 80% code coverage
- **Target**: >95% code coverage
- **Categories**:
  - ✓ Normal cases (positive, negative, decimals)
  - ✓ Boundary conditions (zero, one)
  - ✓ Error cases (exceptions)
  - ✓ Integration cases (combined operations)

---

## Code Quality Standards

### 1. Type Hints

All functions must have type hints:

```python
# Good ✓
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    return a + b

# Bad ✗
def add(a, b):
    return a + b
```

### 2. Docstrings

Use Google-style docstrings:

```python
def factorial(a: Union[int, float]) -> int:
    """
    Return the factorial of a number.

    Args:
        a: The number to compute factorial of

    Returns:
        Factorial of a

    Raises:
        ValueError: If a is not a non-negative integer
    """
```

### 3. Code Formatting

Run Black formatter:

```bash
cd SELab1

# Check formatting (don't modify)
black --check calculator.py test_calculator.py

# Apply formatting
black calculator.py test_calculator.py
```

### 4. Linting

Run Flake8:

```bash
cd SELab1

# Check code style
flake8 calculator.py

# With specific options
flake8 calculator.py --max-line-length=100 --count --statistics
```

### 5. Type Checking

Run MyPy:

```bash
cd SELab1

# Basic type checking
mypy calculator.py

# Strict mode
mypy calculator.py --strict
```

### 6. Quality Check Script

Create and run a complete check:

```bash
#!/bin/bash
cd SELab1

echo "Running tests..."
pytest test_calculator.py -v --cov=. || exit 1

echo "Checking formatting..."
black --check calculator.py test_calculator.py || exit 1

echo "Running linter..."
flake8 calculator.py --max-line-length=100 || exit 1

echo "Type checking..."
mypy calculator.py --strict || exit 1

echo "All checks passed! ✓"
```

---

## Debugging Tips

### 1. Using Print Statements

```python
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    print(f"DEBUG: a={a}, b={b}")
    result = a + b
    print(f"DEBUG: result={result}")
    return result
```

### 2. Using Python Debugger

```python
import pdb

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    pdb.set_trace()  # Execution pauses here
    return a + b
```

### 3. Running Tests with Print Output

```bash
# Show print statements even when tests pass
pytest test_calculator.py -v -s

# Fail and show output
pytest test_calculator.py -v -x
```

### 4. Checking Input Values

```python
def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide two numbers."""
    if b == 0:
        print(f"ERROR: Division by zero. a={a}, b={b}")
        raise ValueError("Cannot divide by zero.")
    return a / b
```

### 5. VS Code Debugging

Add `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["${file}"],
            "console": "integratedTerminal"
        }
    ]
}
```

---

## Common Tasks

### Adding a New Operation

#### Step 1: Implement Function

```python
def new_operation(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Perform new operation on two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Result of operation

    Raises:
        ValueError: If inputs invalid
    """
    if b == 0:
        raise ValueError("Invalid condition")
    return result
```

#### Step 2: Add to Menu

```python
def calculator() -> None:
    """Run the interactive calculator application."""
    
    while True:
        print("Select an operation:")
        # ... existing operations ...
        print("9. New Operation")  # Add new menu item
        print("10. Exit")
        
        choice = input("\nEnter your choice (1-10): ")
        
        if choice == "9":
            num = float(input("Enter number: "))
            try:
                result = new_operation(num)
                print("\nResult:", result)
            except ValueError as error:
                print("Error:", error)
```

#### Step 3: Write Tests

```python
class TestNewOperation:
    """Test cases for new operation."""
    
    def test_basic_case(self):
        assert new_operation(10) == expected
    
    def test_edge_case(self):
        assert new_operation(0) == expected
    
    def test_error_case(self):
        with pytest.raises(ValueError):
            new_operation(invalid_input)
```

#### Step 4: Run All Checks

```bash
pytest test_calculator.py -v --cov=.
black calculator.py test_calculator.py
flake8 calculator.py
mypy calculator.py --strict
```

### Updating Documentation

```bash
# Edit README.md with new operation details
# Update features section
# Add operation to features table
# Update examples

# Commit changes
git add SELab1/README.md
git commit -m "docs: Update README with new operation"
git push origin branch-name
```

### Fixing a Bug

```bash
# Create bug fix branch
git checkout -b bugfix/bug-description

# Make changes to fix bug
# Test the fix
pytest test_calculator.py -v

# Create test case that reproduces bug
# Verify test fails before fix
# Apply fix
# Verify test passes

# Commit
git add .
git commit -m "bugfix: Fix bug description"
git push origin bugfix/bug-description

# Create Pull Request
```

---

## Troubleshooting

### Issue: ModuleNotFoundError

```
ModuleNotFoundError: No module named 'pytest'
```

**Solution**:
```bash
# Ensure virtual environment is activated
# (you should see (venv) in prompt)

# Reinstall requirements
pip install -r SELab1/requirements.txt --force-reinstall
```

### Issue: Tests Fail Unexpectedly

```
FAILED test_calculator.py::TestAddition::test_add_decimals
AssertionError: assert 3.8000000000000003 == 3.8
```

**Solution**: Use `pytest.approx()` for float comparisons:
```python
assert add(1.5, 2.3) == pytest.approx(3.8)
```

### Issue: Black Formatting Conflicts

```
10 file(s) would be reformatted
```

**Solution**:
```bash
# Apply Black formatting
black calculator.py test_calculator.py

# Commit formatted changes
git add .
git commit -m "style: Format code with Black"
```

### Issue: MyPy Strict Mode Errors

```
error: Incompatible types in assignment
```

**Solution**: Add explicit type hints:
```python
# Before
result = divide(10, 5)

# After
result: float = divide(10, 5)
```

### Issue: GitHub Push Rejected

```
error: failed to push some refs to 'origin'
```

**Solution**:
```bash
# Pull latest changes first
git pull origin branch-name

# Resolve any conflicts
# Then push again
git push origin branch-name
```

### Issue: Virtual Environment Not Activating

```bash
# Windows: Try PowerShell instead of Command Prompt
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

# macOS/Linux: Ensure script is executable
chmod +x venv/bin/activate
source venv/bin/activate
```

---

## Best Practices

### 1. Commit Frequently
- Commit logical units of work
- Write meaningful commit messages
- Keep commits focused and small

### 2. Test Before Pushing
```bash
# Always run full test suite before pushing
pytest test_calculator.py -v --cov=.
```

### 3. Keep Branch Updated
```bash
# Regularly sync with main branch
git checkout main
git pull origin main
git checkout your-branch
git merge main
```

### 4. Code Review Checklist

Before creating PR:
- ✓ Code runs without errors
- ✓ All tests pass
- ✓ Code formatted with Black
- ✓ No flake8 warnings
- ✓ Type hints complete
- ✓ Documentation updated
- ✓ Meaningful commit messages

### 5. Helpful Git Aliases

```bash
# Add to git config
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'

# Usage
git co SELab3
git ci -m "message"
git st
```

---

## Additional Resources

### Python Documentation
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Math Module](https://docs.python.org/3/library/math.html)

### Testing
- [pytest Documentation](https://docs.pytest.org/)
- [pytest Coverage](https://pytest-cov.readthedocs.io/)
- [unittest vs pytest](https://docs.pytest.org/en/stable/unittest.html)

### Code Quality
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Style Guide](https://flake8.pycqa.org/)
- [MyPy Type Checker](https://www.mypy-lang.org/)

### Git & GitHub
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [GitHub Markdown](https://docs.github.com/en/github/writing-on-github)

---

## Getting Help

1. **Check Documentation**
   - Review README.md
   - Check TEST_REPORT.md
   - Read PROJECT_SUMMARY.md

2. **Search Issues**
   - GitHub Issues page
   - Similar problems might be solved

3. **Review Code**
   - Check calculator.py
   - Review test_calculator.py
   - Look at existing implementations

4. **Ask Questions**
   - Create GitHub Issue
   - Include error message and steps to reproduce
   - Attach relevant code

---

## Summary

| Task | Command |
|------|---------|
| Setup | `git clone ... && python -m venv venv && pip install -r requirements.txt` |
| Run Calculator | `cd SELab1 && python calculator.py` |
| Run Tests | `pytest test_calculator.py -v --cov=.` |
| Format Code | `black calculator.py test_calculator.py` |
| Lint Code | `flake8 calculator.py` |
| Type Check | `mypy calculator.py --strict` |
| Create Branch | `git checkout -b feature/name` |
| Commit | `git commit -m "message"` |
| Push | `git push origin branch-name` |
| Create PR | Via GitHub web interface |

---

**Last Updated**: August 27, 2026  
**Version**: 1.0  
**Branch**: SELab3  
**Status**: Production Ready
