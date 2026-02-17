# Cosine Similarity

## Description
This module computes the cosine similarity between two 1D arrays.

## Function
```python
def cosine_similarity(a, b)
```

### Parameters
- `a`: 1D numpy array
- `b`: 1D numpy array

### Returns
- `float`: Cosine similarity value in range [-1, 1]

## Example Usage
```python
import numpy as np
from cosine_similarity import cosine_similarity

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = cosine_similarity(a, b)
print(f"Cosine similarity: {result}")
```

## Mathematical Definition
Cosine similarity measures the cosine of the angle between two vectors:
```
cos(θ) = (a · b) / (||a|| * ||b||)
```

Where:
- `a · b` is the dot product
- `||a||` and `||b||` are the L2 norms (magnitudes) of the vectors
