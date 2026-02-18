import numpy as np

def covariance_matrix(X):
    # 1. Ensure X is a numpy array first
    X = np.asarray(X)
    
    # 2. Validation: Must be 2D and have at least 2 samples for N-1 to work
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    
    # 3. Centering
    X_centered = X - np.mean(X, axis=0)
    n_samples = X.shape[0]
    
    # 4. Calculation: (X^T @ X) / (N - 1)
    cov_matrix = (X_centered.T @ X_centered) / (n_samples - 1)
    
    return cov_matrix

# Test with your input
X = [[1, 0], [0, 1]]
print(covariance_matrix(X))