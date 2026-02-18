# Eigenvalues

## Description
This module calculates the eigenvalues of a square matrix.

## Function
```python
def calculate_eigenvalues(matrix)
```

### Parameters
- `matrix`: Square numpy array (n × n)

### Returns
- Numpy array of eigenvalues, or `None` if computation fails

## Example Usage
```python
import numpy as np
from eigenvalues import calculate_eigenvalues

A = np.array([[4, -2], [1, 1]])
eigenvals = calculate_eigenvalues(A)
print(f"Eigenvalues: {eigenvals}")
```

## Mathematical Definition
Eigenvalues λ of a matrix A satisfy:
```
A·v = λ·v
```

Where v is the corresponding eigenvector.

For a 2×2 matrix, eigenvalues are found by solving:
```
det(A - λI) = 0
```
