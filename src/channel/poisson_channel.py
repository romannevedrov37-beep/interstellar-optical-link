import numpy as np


def sample_photon_counts(lambda_: float, size: int, seed: int = None) -> np.ndarray:
    """
    Generate Poisson-distributed photon counts.  #photons_per_slot ≈ 4.5×10⁻⁵
    
    lambda_ : average number of photons expected
    size    : how many samples (slots) to generate
    seed    : optional random seed for reproducibility
    """
    rng = np.random.default_rng(seed)
    return rng.poisson(lambda_, size)

def combined_lambda(lambda_signal: float, lambda_background: float, dark_count_rate: float, pulsed: bool) -> float:
    """
    Combine signal, background, and dark count contributions
    into a single expected photon count for one slot.
    """
    if pulsed == True:
        total_lambda = lambda_signal + lambda_background + dark_count_rate
    else:
        total_lambda = lambda_background + dark_count_rate
    return total_lambda
      