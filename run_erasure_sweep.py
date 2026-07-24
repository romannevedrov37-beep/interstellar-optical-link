import sys
sys.path.append('.')

from src.experiments.uncoded_sweep import run_trial_with_erasures
import numpy as np

rng = np.random.default_rng(42)
bits = rng.integers(0, 2, size=256).tolist()

for rate in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25]:
    result = run_trial_with_erasures(bits, ppm_order=16, erasure_rate=rate, seed=42)
    print(result)