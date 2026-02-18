#!/usr/bin/env python3
"""
Test script to validate all TensorTonic solutions.
"""
import numpy as np
import sys
import os

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def test_dot_product():
    """Test dot product implementation."""
    sys.path.insert(0, 'dot-product')
    exec(open('dot-product/dot-product.py').read(), globals())
    
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    result = dot_product(x, y)
    expected = 32.0
    
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"
    print(f"{GREEN}✓{RESET} dot_product: PASSED")
    return True

def test_cosine_similarity():
    """Test cosine similarity implementation."""
    sys.path.insert(0, 'cosine-similarity')
    exec(open('cosine-similarity/cosine-similarity.py').read(), globals())
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = cosine_similarity(a, b)
    
    # Compute expected value
    expected = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"
    
    # Test zero vector case
    zero = np.array([0, 0, 0])
    result_zero = cosine_similarity(a, zero)
    assert result_zero == 0.0, f"Expected 0.0 for zero vector, got {result_zero}"
    
    print(f"{GREEN}✓{RESET} cosine_similarity: PASSED")
    return True

def test_matrix_transpose():
    """Test matrix transpose implementation."""
    sys.path.insert(0, 'matrix-transpose')
    exec(open('matrix-transpose/matrix-transpose.py').read(), globals())
    
    A = np.array([[1, 2, 3], [4, 5, 6]])
    result = matrix_transpose(A)
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    
    assert np.allclose(result, expected), f"Expected\n{expected}\ngot\n{result}"
    print(f"{GREEN}✓{RESET} matrix_transpose: PASSED")
    return True

def test_euclidean_distance():
    """Test Euclidean distance implementation."""
    sys.path.insert(0, 'euclidean-distance')
    exec(open('euclidean-distance/euclidean-distance.py').read(), globals())
    
    x = [1, 2, 3]
    y = [4, 5, 6]
    result = euclidean_distance(x, y)
    expected = np.sqrt(27)  # sqrt((3)^2 + (3)^2 + (3)^2)
    
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"
    print(f"{GREEN}✓{RESET} euclidean_distance: PASSED")
    return True

def test_manhattan_distance():
    """Test Manhattan distance implementation."""
    sys.path.insert(0, 'manhattan-distance')
    exec(open('manhattan-distance/manhattan-distance.py').read(), globals())
    
    x = [1, 2, 3]
    y = [4, 5, 6]
    result = manhattan_distance(x, y)
    expected = 9.0  # |3| + |3| + |3|
    
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"
    print(f"{GREEN}✓{RESET} manhattan_distance: PASSED")
    return True

def test_eigenvalues():
    """Test eigenvalues calculation."""
    sys.path.insert(0, 'eigenvalues')
    exec(open('eigenvalues/eigenvalues.py').read(), globals())
    
    matrix = np.array([[4, -2], [1, 1]])
    result = calculate_eigenvalues(matrix)
    expected = np.linalg.eigvals(matrix)
    
    assert result is not None, "Expected eigenvalues, got None"
    assert np.allclose(sorted(result), sorted(expected)), f"Expected {expected}, got {result}"
    print(f"{GREEN}✓{RESET} calculate_eigenvalues: PASSED")
    return True

def test_make_diagonal():
    """Test diagonal matrix creation."""
    sys.path.insert(0, 'make-diagonal')
    exec(open('make-diagonal/make-diagonal.py').read(), globals())
    
    v = np.array([1, 2, 3])
    result = make_diagonal(v)
    expected = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    
    assert np.allclose(result, expected), f"Expected\n{expected}\ngot\n{result}"
    print(f"{GREEN}✓{RESET} make_diagonal: PASSED")
    return True

def test_matrix_inverse():
    """Test matrix inverse calculation."""
    sys.path.insert(0, 'matrix-inverse')
    exec(open('matrix-inverse/matrix-inverse.py').read(), globals())
    
    A = np.array([[4, 7], [2, 6]])
    result = matrix_inverse(A)
    
    assert result is not None, "Expected inverse matrix, got None"
    identity = np.eye(2)
    product = A @ result
    assert np.allclose(product, identity), f"A @ A_inv should equal I, got\n{product}"
    print(f"{GREEN}✓{RESET} matrix_inverse: PASSED")
    return True

def test_matrix_trace():
    """Test matrix trace calculation."""
    sys.path.insert(0, 'matrix-trace')
    exec(open('matrix-trace/matrix-trace.py').read(), globals())
    
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result = matrix_trace(A)
    expected = 15  # 1 + 5 + 9
    
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"{GREEN}✓{RESET} matrix_trace: PASSED")
    return True

def main():
    """Run all tests."""
    print(f"\n{BLUE}Running TensorTonic Solutions Tests{RESET}\n")
    print("=" * 50)
    
    tests = [
        test_dot_product,
        test_cosine_similarity,
        test_matrix_transpose,
        test_euclidean_distance,
        test_manhattan_distance,
        test_eigenvalues,
        test_make_diagonal,
        test_matrix_inverse,
        test_matrix_trace
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            failed += 1
            print(f"{RED}✗{RESET} {test.__name__}: FAILED - {str(e)}")
    
    print("\n" + "=" * 50)
    print(f"\n{BLUE}Test Summary:{RESET}")
    print(f"  {GREEN}Passed:{RESET} {passed}/{len(tests)}")
    if failed > 0:
        print(f"  {RED}Failed:{RESET} {failed}/{len(tests)}")
        sys.exit(1)
    else:
        print(f"\n{GREEN}All tests passed!{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
