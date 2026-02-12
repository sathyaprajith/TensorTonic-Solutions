import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    try:   
        inverse = np.linalg.inv(A)
        identity = np.eye(len(A))
        if not(np.allclose(A @ inverse,identity)):
            return None
            
        return inverse
    except np.linalg.LinAlgError:
        return None
