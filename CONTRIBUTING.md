# Contributing to TensorTonic Solutions

Thank you for your interest in contributing to this repository! This guide will help you get started.

## About This Repository

This repository contains solutions to machine learning and deep learning problems from [TensorTonic](https://tensortonic.com), a platform where you can implement core algorithms from scratch.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- NumPy library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sathyaprajith/TensorTonic-Solutions.git
cd TensorTonic-Solutions
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests to verify everything works:
```bash
python test_all.py
```

## Project Structure

Each solution is organized in its own directory:

```
TensorTonic-Solutions/
├── dot-product/
│   ├── dot-product.py
│   └── README.md
├── cosine-similarity/
│   ├── cosine-similarity.py
│   └── README.md
├── matrix-transpose/
│   ├── matrix-transpose.py
│   └── README.md
...
```

## Adding a New Solution

When adding a new solution:

1. Create a new directory with a descriptive name (e.g., `matrix-multiplication/`)

2. Add your Python implementation:
   - Name the file consistently (e.g., `matrix-multiplication.py`)
   - Include proper docstrings
   - Use NumPy for mathematical operations
   - Follow the existing code style

3. Add a README.md file with:
   - Description of the algorithm
   - Function signature and parameters
   - Example usage
   - Mathematical definition

4. Update the main README.md if needed

5. Add tests to `test_all.py` to validate your solution

## Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable names
- Add docstrings to all functions
- Keep functions focused and simple
- Use type hints where appropriate

## Testing

Before submitting any changes:

1. Run all tests:
```bash
python test_all.py
```

2. Verify your solution handles edge cases:
   - Empty arrays
   - Zero values
   - Singular matrices (for matrix operations)
   - Invalid inputs

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-solution`)
3. Make your changes
4. Run tests to ensure everything works
5. Commit your changes with clear messages
6. Push to your fork
7. Create a Pull Request

## Questions or Issues?

If you have questions or find issues:

- Open an issue on GitHub
- Provide clear details about the problem
- Include steps to reproduce (if applicable)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Happy coding! 🚀
