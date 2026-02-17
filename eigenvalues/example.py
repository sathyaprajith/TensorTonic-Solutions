#!/usr/bin/env python3
"""
Example usage of the calculate_eigenvalues function.
"""
import numpy as np

# Load the function
exec(open('eigenvalues.py').read())

print("=" * 50)
print("Eigenvalues Calculation Examples")
print("=" * 50)

# Example 1: Simple 2x2 matrix
print("\nExample 1: Simple 2x2 matrix")
matrix = np.array([[4, -2], [1, 1]])
eigenvals = calculate_eigenvalues(matrix)
print("Matrix:")
print(matrix)
print(f"Eigenvalues: {eigenvals}")

# Example 2: Identity matrix
print("\nExample 2: Identity matrix")
matrix = np.eye(3)
eigenvals = calculate_eigenvalues(matrix)
print("Matrix (Identity):")
print(matrix)
print(f"Eigenvalues: {eigenvals}")
print("(All eigenvalues should be 1)")

# Example 3: Diagonal matrix
print("\nExample 3: Diagonal matrix")
matrix = np.diag([2, 3, 5])
eigenvals = calculate_eigenvalues(matrix)
print("Matrix (Diagonal):")
print(matrix)
print(f"Eigenvalues: {eigenvals}")
print("(Eigenvalues should be diagonal elements)")

# Example 4: Symmetric matrix
print("\nExample 4: Symmetric matrix")
matrix = np.array([[6, -2, 0], [-2, 7, -1], [0, -1, 8]])
eigenvals = calculate_eigenvalues(matrix)
print("Matrix (Symmetric):")
print(matrix)
print(f"Eigenvalues: {eigenvals}")
print(f"All real? {np.all(np.isreal(eigenvals))}")

# Example 5: Rotation matrix
print("\nExample 5: 2D Rotation matrix (90 degrees)")
theta = np.pi / 2
matrix = np.array([[np.cos(theta), -np.sin(theta)], 
                   [np.sin(theta), np.cos(theta)]])
eigenvals = calculate_eigenvalues(matrix)
print("Matrix (90° rotation):")
print(matrix)
print(f"Eigenvalues: {eigenvals}")
print("(Complex eigenvalues for rotation)")

# Example 6: Zero matrix
print("\nExample 6: Zero matrix")
matrix = np.zeros((3, 3))
eigenvals = calculate_eigenvalues(matrix)
print("Matrix (All zeros):")
print(matrix)
print(f"Eigenvalues: {eigenvals}")
print("(All eigenvalues should be 0)")

# Example 7: Trace property
print("\nExample 7: Trace property verification")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
eigenvals = calculate_eigenvalues(matrix)
trace = np.trace(matrix)
sum_eigenvals = np.sum(eigenvals)
print("Matrix:")
print(matrix)
print(f"Trace of matrix: {trace:.4f}")
print(f"Sum of eigenvalues: {sum_eigenvals:.4f}")
print(f"They match: {np.isclose(trace, sum_eigenvals)}")

print("\n" + "=" * 50)
