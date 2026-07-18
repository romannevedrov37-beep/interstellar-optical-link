from dataclasses import dataclass
import numpy as np


@dataclass
class SNSPDDetector:
    """Simplified model of an SNSPD-like single-photon detector."""
    eta: float
    dark_rate: float
    jitter_ps: float = 0.0
    max_count_rate: float = None

    def observe(self, true_photon_counts: np.ndarray, seed: int = None) -> np.ndarray:
        """
        Given the true number of photons per slot, simulate what the
        detector actually registers (accounting for efficiency and dark counts).
        """
        rng = np.random.default_rng(seed)

        detected_signal = rng.binomial(true_photon_counts, self.eta)
        dark_counts = rng.poisson(self.dark_rate, size=len(true_photon_counts))

        return detected_signal + dark_counts

    def apply_jitter(self, frame: np.ndarray, jitter_probability: float, seed: int = None) -> np.ndarray:
        """
        With some probability, shift the pulse to an adjacent slot,
        simulating timing jitter.
        """
        rng = np.random.default_rng(seed)
        frame = frame.copy()

        pulse_positions = np.where(frame == 1)[0]

        for pos in pulse_positions:
            if rng.random() < jitter_probability:
                shift = rng.choice([-1, 1])
                new_pos = pos + shift

                if 0 <= new_pos < len(frame):
                    frame[pos] = 0
                    frame[new_pos] = 1

        return frame