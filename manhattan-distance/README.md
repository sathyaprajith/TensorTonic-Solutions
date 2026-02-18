# Manhattan Distance

## Description
This module computes the Manhattan (L1) distance between two vectors.

## Function
```python
def manhattan_distance(x, y)
```

### Parameters
- `x`: 1D array-like (list or numpy array)
- `y`: 1D array-like (list or numpy array)

### Returns
- `float`: The Manhattan distance between x and y

## Example Usage
```python
import numpy as np
from manhattan_distance import manhattan_distance

x = [1, 2, 3]
y = [4, 5, 6]
result = manhattan_distance(x, y)
print(f"Manhattan distance: {result}")
```

## Mathematical Definition
The Manhattan distance (L1 norm) is defined as:
```
d(x, y) = Σ|x_i - y_i|
```

Also known as the taxicab distance or city block distance, it represents the sum of absolute differences between corresponding elements.
