import sys
sys.path.append('.')

import numpy as np
from src.detector.snspd_model import SNSPDDetector

detector = SNSPDDetector(eta=0.8, dark_rate=0.001)

true_photon_counts = np.array([1, 2, 3, 0, 0, 2, 1, 0, 0, 1]) #взяли рандомные

observed_counts = detector.observe(true_photon_counts, seed=42)

print(f"True photon counts: {true_photon_counts}")
print(f"Observed counts: {observed_counts}")