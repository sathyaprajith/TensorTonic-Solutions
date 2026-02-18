# Matrix Trace

## Description
This module computes the trace of a square matrix (sum of diagonal elements).

## Function
```python
def matrix_trace(A)
```

### Parameters
- `A`: Square numpy array (n × n)

### Returns
- Scalar value representing the trace of the matrix

## Example Usage
```python
import numpy as np
from matrix_trace import matrix_trace

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
trace = matrix_trace(A)
print(f"Trace of matrix: {trace}")  # Output: 15
```

## Mathematical Definition
The trace of a matrix is the sum of its diagonal elements:
```
tr(A) = Σ A[i, i] for i = 0 to n-1
```

### Properties
- tr(A + B) = tr(A) + tr(B)
- tr(cA) = c·tr(A) for scalar c
- tr(A^T) = tr(A)
- tr(AB) = tr(BA)
