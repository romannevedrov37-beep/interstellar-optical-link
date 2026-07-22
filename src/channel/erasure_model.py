import numpy as np


def generate_erasure_mask(num_symbols: int, erasure_rate: float, seed: int = None) -> np.ndarray:
    """
    Generate an iid Bernoulli erasure mask: True means the symbol at
    that position is erased (lost), independently with probability
    erasure_rate.
    """
    rng = np.random.default_rng(seed)
    random_numbers = rng.random(num_symbols)
    mask = random_numbers < erasure_rate
    return mask