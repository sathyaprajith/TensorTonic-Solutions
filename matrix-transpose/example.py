#!/usr/bin/env python3
"""
Example usage of the matrix_transpose function.
"""
import numpy as np

# Load the function
exec(open('matrix-transpose.py').read())

print("=" * 50)
print("Matrix Transpose Examples")
print("=" * 50)

# Example 1: Rectangular matrix
print("\nExample 1: 2x3 matrix")
A = np.array([[1, 2, 3], [4, 5, 6]])
result = matrix_transpose(A)
print("Original matrix (2x3):")
print(A)
print("\nTransposed matrix (3x2):")
print(result)

# Example 2: Square matrix
print("\nExample 2: 3x3 square matrix")
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix_transpose(A)
print("Original matrix:")
print(A)
print("\nTransposed matrix:")
print(result)

# Example 3: Row vector
print("\nExample 3: Row vector (1x4)")
A = np.array([[1, 2, 3, 4]])
result = matrix_transpose(A)
print("Original (row vector):")
print(A)
print("\nTransposed (column vector):")
print(result)

# Example 4: Symmetric matrix
print("\nExample 4: Symmetric matrix")
A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
result = matrix_transpose(A)
print("Original symmetric matrix:")
print(A)
print("\nTransposed (should be identical):")
print(result)
print(f"Is symmetric? {np.allclose(A, result)}")

# Example 5: Double transpose
print("\nExample 5: Double transpose")
A = np.array([[1, 2], [3, 4], [5, 6]])
result = matrix_transpose(matrix_transpose(A))
print("Original matrix:")
print(A)
print("\nDouble transposed (should equal original):")
print(result)
print(f"Equals original? {np.allclose(A, result)}")

print("\n" + "=" * 50)
