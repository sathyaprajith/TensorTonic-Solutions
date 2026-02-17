#!/usr/bin/env python3
"""
Example usage of the matrix_trace function.
"""
import numpy as np

# Load the function
exec(open('matrix-trace.py').read())

print("=" * 50)
print("Matrix Trace Examples")
print("=" * 50)

# Example 1: Simple 3x3 matrix
print("\nExample 1: Simple 3x3 matrix")
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
trace = matrix_trace(A)
print("Matrix A:")
print(A)
print(f"Trace: {trace}")
print(f"Calculation: 1 + 5 + 9 = {trace}")

# Example 2: Identity matrix
print("\nExample 2: Identity matrix")
A = np.eye(4)
trace = matrix_trace(A)
print(f"4x4 Identity matrix")
print("Matrix A:")
print(A)
print(f"Trace: {trace}")
print("(Trace of nxn identity matrix = n)")

# Example 3: Diagonal matrix
print("\nExample 3: Diagonal matrix")
A = np.diag([2, 3, 5, 7])
trace = matrix_trace(A)
print("Matrix A (Diagonal):")
print(A)
print(f"Trace: {trace}")
print(f"Sum of diagonal: {np.sum([2, 3, 5, 7])}")

# Example 4: Zero matrix
print("\nExample 4: Zero matrix")
A = np.zeros((3, 3))
trace = matrix_trace(A)
print("Matrix A (All zeros):")
print(A)
print(f"Trace: {trace}")

# Example 5: Symmetric matrix
print("\nExample 5: Symmetric matrix")
A = np.array([[4, 1, 2], [1, 5, 3], [2, 3, 6]])
trace = matrix_trace(A)
print("Matrix A (Symmetric):")
print(A)
print(f"Trace: {trace}")

# Example 6: Trace properties
print("\nExample 6: Trace properties")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print(f"\ntr(A) = {matrix_trace(A)}")
print(f"tr(B) = {matrix_trace(B)}")
print(f"tr(A + B) = {matrix_trace(A + B)}")
print(f"tr(A) + tr(B) = {matrix_trace(A) + matrix_trace(B)}")
print(f"Property verified: tr(A + B) = tr(A) + tr(B): {matrix_trace(A + B) == matrix_trace(A) + matrix_trace(B)}")

# Example 7: Trace and eigenvalues
print("\nExample 7: Trace and eigenvalues relationship")
A = np.array([[4, -2], [1, 1]])
trace = matrix_trace(A)
eigenvals = np.linalg.eigvals(A)
print("Matrix A:")
print(A)
print(f"Trace: {trace}")
print(f"Eigenvalues: {eigenvals}")
print(f"Sum of eigenvalues: {np.sum(eigenvals):.4f}")
print(f"Property: trace = sum of eigenvalues: {np.isclose(trace, np.sum(eigenvals))}")

# Example 8: Scalar multiplication
print("\nExample 8: Scalar multiplication")
A = np.array([[2, 3], [4, 5]])
c = 3
print("Matrix A:")
print(A)
print(f"Scalar c = {c}")
print(f"tr(A) = {matrix_trace(A)}")
print(f"tr(cA) = {matrix_trace(c * A)}")
print(f"c × tr(A) = {c * matrix_trace(A)}")
print(f"Property verified: tr(cA) = c × tr(A): {matrix_trace(c * A) == c * matrix_trace(A)}")

print("\n" + "=" * 50)
