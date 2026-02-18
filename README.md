# TensorTonic Solutions

Welcome to my TensorTonic solutions repository! 🚀

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, demonstrating fundamental linear algebra and machine learning concepts.

## 📚 Solutions Included

### Distance Metrics
- **[Euclidean Distance](/euclidean-distance)** - L2 norm distance between vectors
- **[Manhattan Distance](/manhattan-distance)** - L1 norm (taxicab) distance
- **[Cosine Similarity](/cosine-similarity)** - Measure of similarity between vectors

### Vector Operations
- **[Dot Product](/dot-product)** - Scalar product of two vectors

### Matrix Operations
- **[Matrix Transpose](/matrix-transpose)** - Swap rows and columns
- **[Matrix Trace](/matrix-trace)** - Sum of diagonal elements
- **[Matrix Inverse](/matrix-inverse)** - Find the inverse of a matrix
- **[Make Diagonal](/make-diagonal)** - Create diagonal matrix from vector
- **[Eigenvalues](/eigenvalues)** - Calculate eigenvalues of a matrix

## 🚀 Quick Start

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

3. Run tests to validate all solutions:
```bash
python test_all.py
```

## 💡 Usage

Each solution is in its own directory with:
- **Implementation file** (`*.py`) - The core algorithm
- **README** - Detailed documentation and mathematical definitions
- **Example script** (`example.py`) - Demonstrates usage with multiple examples

### Example: Using Dot Product

```python
import numpy as np
exec(open('dot-product/dot-product.py').read())

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = dot_product(x, y)
print(f"Dot product: {result}")  # Output: 32.0
```

Or run the example script:
```bash
cd dot-product
python example.py
```

## 🧪 Testing

Run all tests with:
```bash
python test_all.py
```

This will validate all implementations with multiple test cases.

## 📖 Documentation

Each solution directory contains:
- Detailed README with mathematical definitions
- Example usage scripts
- Implementation with docstrings

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is open source and available for educational purposes.

## 🔗 Links

- [TensorTonic Platform](https://tensortonic.com) - Practice ML algorithms from scratch
- [Repository Issues](https://github.com/sathyaprajith/TensorTonic-Solutions/issues) - Report bugs or request features

---

⭐ If you find this repository helpful, please consider giving it a star!
