import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    numpy_matrix = np.asarray([np.asarray(l) for l in A])
    return numpy_matrix.T
