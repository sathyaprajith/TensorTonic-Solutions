# Matrix Inverse

## Description
This module computes the inverse of a square matrix.

## Function
```python
def matrix_inverse(A)
```

### Parameters
- `A`: Square numpy array (n × n)

### Returns
- `A_inv`: Inverse matrix such that A @ A_inv ≈ I, or `None` if matrix is singular

## Example Usage
```python
import numpy as np
from matrix_inverse import matrix_inverse

A = np.array([[4, 7], [2, 6]])
A_inv = matrix_inverse(A)
if A_inv is not None:
    print("Inverse matrix:")
    print(A_inv)
    print("Verification A @ A_inv:")
    print(A @ A_inv)
```

## Mathematical Definition
For a matrix A, its inverse A^(-1) satisfies:
```
A · A^(-1) = A^(-1) · A = I
```

Where I is the identity matrix.

**Note**: Only non-singular (invertible) matrices have an inverse. A matrix is invertible if and only if its determinant is non-zero.
