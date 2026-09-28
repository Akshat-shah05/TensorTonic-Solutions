import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    np_a, np_b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    dot = np.dot(np_a, np_b)
    a_mag, b_mag = np.linalg.norm(a), np.linalg.norm(b)
    if (a_mag == 0) or (b_mag == 0):
        return 0.0

    return float(np.dot(a, b)/(a_mag * b_mag))