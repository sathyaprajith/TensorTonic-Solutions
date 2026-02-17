#!/usr/bin/env python3
"""
Example usage of the cosine_similarity function.
"""
import numpy as np

# Load the function
exec(open('cosine-similarity.py').read())

print("=" * 50)
print("Cosine Similarity Examples")
print("=" * 50)

# Example 1: Similar vectors
print("\nExample 1: Similar vectors")
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
result = cosine_similarity(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"Cosine similarity = {result:.4f} (identical direction)")

# Example 2: Orthogonal vectors
print("\nExample 2: Orthogonal vectors")
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
result = cosine_similarity(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"Cosine similarity = {result:.4f} (perpendicular)")

# Example 3: Opposite vectors
print("\nExample 3: Opposite vectors")
a = np.array([1, 2, 3])
b = np.array([-1, -2, -3])
result = cosine_similarity(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"Cosine similarity = {result:.4f} (opposite direction)")

# Example 4: General case
print("\nExample 4: General vectors")
a = np.array([3, 4])
b = np.array([4, 3])
result = cosine_similarity(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"Cosine similarity = {result:.4f}")
angle_deg = np.degrees(np.arccos(result))
print(f"Angle between vectors: {angle_deg:.2f}°")

# Example 5: Zero vector
print("\nExample 5: Zero vector handling")
a = np.array([1, 2, 3])
b = np.array([0, 0, 0])
result = cosine_similarity(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"Cosine similarity = {result:.4f} (zero vector case)")

print("\n" + "=" * 50)
