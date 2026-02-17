#!/usr/bin/env python3
"""
Example usage of the euclidean_distance function.
"""
import numpy as np

# Load the function
exec(open('euclidean-distance.py').read())

print("=" * 50)
print("Euclidean Distance Examples")
print("=" * 50)

# Example 1: 2D points
print("\nExample 1: Distance between 2D points")
x = [0, 0]
y = [3, 4]
result = euclidean_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Euclidean distance = {result:.4f}")

# Example 2: 3D points
print("\nExample 2: Distance between 3D points")
x = [1, 2, 3]
y = [4, 5, 6]
result = euclidean_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Euclidean distance = {result:.4f}")

# Example 3: Identical points
print("\nExample 3: Identical points")
x = [5, 10, 15]
y = [5, 10, 15]
result = euclidean_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Euclidean distance = {result:.4f} (should be 0)")

# Example 4: High-dimensional vectors
print("\nExample 4: High-dimensional vectors")
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
result = euclidean_distance(x, y)
print(f"Vector 1: {x}")
print(f"Vector 2: {y}")
print(f"Euclidean distance = {result:.4f}")

# Example 5: Unit circle points
print("\nExample 5: Points on unit circle")
x = [1, 0]
y = [0, 1]
result = euclidean_distance(x, y)
print(f"Point 1 (on unit circle): {x}")
print(f"Point 2 (on unit circle): {y}")
print(f"Euclidean distance = {result:.4f}")
print(f"Expected (sqrt(2)) = {np.sqrt(2):.4f}")

print("\n" + "=" * 50)
