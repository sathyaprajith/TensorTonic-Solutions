import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    Assumes X is (N samples, M features).
    """
    # X_centered = X - np.mean(X, axis=0)
    # covariance = np.cov(X, rowvar=False)
    # std_dev = np.std(X, axis=0)
    return np.corrcoef(X, rowvar=False)