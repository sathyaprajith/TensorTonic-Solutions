#!/usr/bin/env python3
"""
Example usage of the make_diagonal function.
"""
import numpy as np

# Load the function
exec(open('make-diagonal.py').read())

print("=" * 50)
print("Make Diagonal Matrix Examples")
print("=" * 50)

# Example 1: Simple diagonal matrix
print("\nExample 1: 3x3 diagonal matrix")
v = np.array([1, 2, 3])
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Diagonal matrix:")
print(result)

# Example 2: 2x2 diagonal matrix
print("\nExample 2: 2x2 diagonal matrix")
v = np.array([5, 10])
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Diagonal matrix:")
print(result)

# Example 3: Identity matrix
print("\nExample 3: Identity matrix (all ones)")
v = np.ones(4)
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Diagonal matrix (Identity):")
print(result)

# Example 4: Scaling matrix
print("\nExample 4: Scaling matrix")
v = np.array([2, 3, 4])
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Scaling matrix:")
print(result)
test_point = np.array([1, 1, 1])
scaled = result @ test_point
print(f"\nScaling point {test_point}:")
print(f"Result: {scaled}")

# Example 5: Zero diagonal
print("\nExample 5: Zero diagonal matrix")
v = np.zeros(3)
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Zero matrix:")
print(result)

# Example 6: Single element
print("\nExample 6: 1x1 diagonal matrix")
v = np.array([42])
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Diagonal matrix:")
print(result)

# Example 7: Negative values
print("\nExample 7: Diagonal with negative values")
v = np.array([-1, 2, -3, 4])
result = make_diagonal(v)
print(f"Input vector: {v}")
print("Diagonal matrix:")
print(result)

# Example 8: Using in matrix operations
print("\nExample 8: Diagonal matrix properties")
v = np.array([2, 3, 5])
D = make_diagonal(v)
print(f"Diagonal matrix D:")
print(D)
print(f"\nTrace of D: {np.trace(D)} (sum of diagonal elements)")
print(f"Sum of vector: {np.sum(v)}")
print(f"Determinant of D: {np.linalg.det(D)} (product of diagonal elements)")
print(f"Product of vector: {np.prod(v)}")

print("\n" + "=" * 50)
