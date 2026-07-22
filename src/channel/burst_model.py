import numpy as np


def generate_burst_mask(num_symbols: int, burst_length: int, seed: int = None) -> np.ndarray:
    """
    Generate a mask with one contiguous burst of erasures of the given
    length, starting at a random position.
    """
    rng = np.random.default_rng(seed)
    mask = np.zeros(num_symbols, dtype=bool)

    start = rng.integers(0, num_symbols - burst_length)
    end = start + burst_length

    mask[start:end] = True
    return mask