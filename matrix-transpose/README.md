# Matrix Transpose

## Description
This module returns the transpose of a matrix (swaps rows and columns).

## Function
```python
def matrix_transpose(A)
```

### Parameters
- `A`: 2D numpy array (matrix)

### Returns
- Transposed matrix where rows become columns and vice versa

## Example Usage
```python
import numpy as np
from matrix_transpose import matrix_transpose

A = np.array([[1, 2, 3], [4, 5, 6]])
result = matrix_transpose(A)
print("Original matrix:")
print(A)
print("Transposed matrix:")
print(result)
```

## Mathematical Definition
For a matrix A with dimensions (m, n), the transpose A^T has dimensions (n, m) where:
```
A^T[i, j] = A[j, i]
```
