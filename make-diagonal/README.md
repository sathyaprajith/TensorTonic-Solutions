# Make Diagonal

## Description
This module creates a diagonal matrix from a 1D array.

## Function
```python
def make_diagonal(v)
```

### Parameters
- `v`: 1D numpy array of length n

### Returns
- (n, n) numpy array with v on the main diagonal and zeros elsewhere

## Example Usage
```python
import numpy as np
from make_diagonal import make_diagonal

v = np.array([1, 2, 3])
result = make_diagonal(v)
print("Diagonal matrix:")
print(result)
# Output:
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
```

## Mathematical Definition
Creates a diagonal matrix D from vector v where:
```
D[i, j] = v[i] if i == j
D[i, j] = 0   if i != j
```
