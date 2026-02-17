#!/usr/bin/env python3
"""
Example usage of the matrix_inverse function.
"""
import numpy as np

# Load the function
exec(open('matrix-inverse.py').read())

print("=" * 50)
print("Matrix Inverse Examples")
print("=" * 50)

# Example 1: Simple 2x2 matrix
print("\nExample 1: Simple 2x2 matrix")
A = np.array([[4, 7], [2, 6]])
A_inv = matrix_inverse(A)
print("Matrix A:")
print(A)
print("\nInverse A^(-1):")
print(A_inv)
print("\nVerification A @ A^(-1):")
print(A @ A_inv)

# Example 2: 3x3 matrix
print("\nExample 2: 3x3 matrix")
A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
A_inv = matrix_inverse(A)
if A_inv is not None:
    print("Matrix A:")
    print(A)
    print("\nInverse A^(-1):")
    print(A_inv)
    print("\nVerification A @ A^(-1):")
    print(A @ A_inv)

# Example 3: Identity matrix
print("\nExample 3: Identity matrix")
A = np.eye(3)
A_inv = matrix_inverse(A)
print("Matrix A (Identity):")
print(A)
print("\nInverse A^(-1) (should be itself):")
print(A_inv)

# Example 4: Diagonal matrix
print("\nExample 4: Diagonal matrix")
A = np.diag([2, 3, 4])
A_inv = matrix_inverse(A)
print("Matrix A (Diagonal):")
print(A)
print("\nInverse A^(-1) (reciprocals on diagonal):")
print(A_inv)

# Example 5: Singular matrix (no inverse)
print("\nExample 5: Singular matrix (no inverse)")
A = np.array([[1, 2], [2, 4]])
A_inv = matrix_inverse(A)
print("Matrix A (Singular):")
print(A)
print(f"Determinant: {np.linalg.det(A):.6f}")
print(f"Inverse: {A_inv}")
print("(None because matrix is singular)")

# Example 6: Solving linear equations
print("\nExample 6: Solving linear equations Ax = b")
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 11])
A_inv = matrix_inverse(A)
x = A_inv @ b
print("System: Ax = b")
print("Matrix A:")
print(A)
print(f"\nVector b: {b}")
print(f"Solution x = A^(-1)b: {x}")
print(f"Verification Ax: {A @ x}")

# Example 7: Orthogonal matrix
print("\nExample 7: Orthogonal matrix (rotation)")
theta = np.pi / 4  # 45 degrees
A = np.array([[np.cos(theta), -np.sin(theta)], 
              [np.sin(theta), np.cos(theta)]])
A_inv = matrix_inverse(A)
print("Matrix A (Rotation 45°):")
print(A)
print("\nInverse A^(-1):")
print(A_inv)
print("\nTranspose A^T:")
print(A.T)
print(f"\nFor orthogonal matrices, A^(-1) = A^T: {np.allclose(A_inv, A.T)}")

print("\n" + "=" * 50)
