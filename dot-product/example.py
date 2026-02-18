#!/usr/bin/env python3
"""
Example usage of the dot_product function.
"""
import numpy as np

# Load the function
exec(open('dot-product.py').read())

print("=" * 50)
print("Dot Product Examples")
print("=" * 50)

# Example 1: Simple vectors
print("\nExample 1: Simple vectors")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = dot_product(x, y)
print(f"x = {x}")
print(f"y = {y}")
print(f"x · y = {result}")

# Example 2: Orthogonal vectors (dot product = 0)
print("\nExample 2: Orthogonal vectors")
x = np.array([1, 0])
y = np.array([0, 1])
result = dot_product(x, y)
print(f"x = {x}")
print(f"y = {y}")
print(f"x · y = {result} (orthogonal)")

# Example 3: Parallel vectors
print("\nExample 3: Parallel vectors")
x = np.array([2, 4, 6])
y = np.array([1, 2, 3])
result = dot_product(x, y)
print(f"x = {x}")
print(f"y = {y}")
print(f"x · y = {result}")

# Example 4: Longer vectors
print("\nExample 4: Longer vectors")
x = np.array([1, -2, 3, -4, 5])
y = np.array([2, 3, -1, 4, 2])
result = dot_product(x, y)
print(f"x = {x}")
print(f"y = {y}")
print(f"x · y = {result}")

print("\n" + "=" * 50)
