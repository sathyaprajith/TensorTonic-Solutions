# Dot Product

## Description
This module computes the dot product of two 1D arrays.

## Function
```python
def dot_product(x, y)
```

### Parameters
- `x`: 1D numpy array
- `y`: 1D numpy array

### Returns
- `float`: The dot product of x and y

## Example Usage
```python
import numpy as np
from dot_product import dot_product

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = dot_product(x, y)
print(f"Dot product: {result}")  # Output: 32.0
```

## Mathematical Definition
The dot product of two vectors is defined as:
```
x · y = Σ(x_i * y_i)
```
