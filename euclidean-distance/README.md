# Euclidean Distance

## Description
This module computes the Euclidean (L2) distance between two vectors.

## Function
```python
def euclidean_distance(x, y)
```

### Parameters
- `x`: 1D array-like (list or numpy array)
- `y`: 1D array-like (list or numpy array)

### Returns
- `float`: The Euclidean distance between x and y

## Example Usage
```python
import numpy as np
from euclidean_distance import euclidean_distance

x = [1, 2, 3]
y = [4, 5, 6]
result = euclidean_distance(x, y)
print(f"Euclidean distance: {result}")
```

## Mathematical Definition
The Euclidean distance (L2 norm) is defined as:
```
d(x, y) = √(Σ(x_i - y_i)²)
```

This represents the straight-line distance between two points in Euclidean space.
