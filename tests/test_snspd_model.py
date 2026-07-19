import sys
sys.path.append('.')

import numpy as np
from src.detector.snspd_model import SNSPDDetector

detector = SNSPDDetector(eta=0.8, dark_rate=0.001)

true_photon_counts = np.array([1, 2, 3, 0, 0, 2, 1, 0, 0, 1]) #взяли рандомные

observed_counts = detector.observe(true_photon_counts, seed=42)

print(f"True photon counts: {true_photon_counts}")
print(f"Observed counts: {observed_counts}")

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
from src.modem.ppm_encoder import PPMEncoder

encoder = PPMEncoder(ppm_order=16)
frame = encoder.encode_symbol([1, 0, 1, 0])
print(f"Before jitter: {frame}")

jittered = detector.apply_jitter(frame, jitter_probability=0.9, seed=2)
print(f"After jitter:  {jittered}")