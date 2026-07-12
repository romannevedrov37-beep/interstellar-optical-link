from dataclasses import dataclass
import numpy as np


@dataclass
class SNSPDDetector:
    """Simplified model of an SNSPD-like single-photon detector."""
    eta: float               # detection efficiency, 0 to 1
    dark_rate: float         # average dark counts per slot
    jitter_ps: float = 0.0        # reserved for future timing jitter modeling (not used in v0)
    max_count_rate: float = None  # reserved for future dead-time modeling (not used in v0)

    def observe(self, true_photon_counts: np.ndarray, seed: int = None) -> np.ndarray:
        """
        Given the true number of photons per slot, simulate what the
        detector actually registers (accounting for efficiency and dark counts).
        """
        rng = np.random.default_rng(seed)
        detected_signal = rng.binomial(true_photon_counts, self.eta)
        dark_counts = rng.poisson(self.dark_rate, size=len(true_photon_counts))
    
        return detected_signal + dark_counts