#!/usr/bin/env python3
"""
Example usage of the manhattan_distance function.
"""
import numpy as np

# Load the function
exec(open('manhattan-distance.py').read())

print("=" * 50)
print("Manhattan Distance Examples")
print("=" * 50)

# Example 1: City grid navigation
print("\nExample 1: City grid navigation")
x = [0, 0]
y = [3, 4]
result = manhattan_distance(x, y)
print(f"Start point: {x}")
print(f"End point: {y}")
print(f"Manhattan distance = {result:.0f} blocks")
print("(Move 3 blocks right + 4 blocks up)")

# Example 2: 3D points
print("\nExample 2: Distance between 3D points")
x = [1, 2, 3]
y = [4, 5, 6]
result = manhattan_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Manhattan distance = {result:.0f}")

# Example 3: Identical points
print("\nExample 3: Identical points")
x = [5, 10, 15]
y = [5, 10, 15]
result = manhattan_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Manhattan distance = {result:.0f} (should be 0)")

# Example 4: Negative coordinates
print("\nExample 4: Points with negative coordinates")
x = [-3, -4]
y = [3, 4]
result = manhattan_distance(x, y)
print(f"Point 1: {x}")
print(f"Point 2: {y}")
print(f"Manhattan distance = {result:.0f}")

# Example 5: High-dimensional space
print("\nExample 5: High-dimensional vectors")
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
result = manhattan_distance(x, y)
print(f"Vector 1: {x}")
print(f"Vector 2: {y}")
print(f"Manhattan distance = {result:.0f}")

# Comparison with Euclidean
print("\nBonus: Comparison with Euclidean distance")
from numpy.linalg import norm
x = [0, 0]
y = [3, 4]
manhattan = manhattan_distance(x, y)
euclidean = norm(np.array(y) - np.array(x))
print(f"Points: {x} to {y}")
print(f"Manhattan distance: {manhattan:.2f}")
print(f"Euclidean distance: {euclidean:.2f}")
print(f"Manhattan ≥ Euclidean: {manhattan >= euclidean}")

print("\n" + "=" * 50)
