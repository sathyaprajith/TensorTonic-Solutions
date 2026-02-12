import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        vals = np.linalg.eigvals(matrix)
        return vals
    except (np.linalg.LinAlgError,ValueError):
        return None
