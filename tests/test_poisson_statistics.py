import sys
sys.path.append('.')

import numpy as np
from src.channel.poisson_channel import sample_photon_counts

lambda_test = 0.55
samples = sample_photon_counts(lambda_test, size=10000, seed=42)
sample_mean = np.mean(samples)     
sample_variance = np.var(samples)

print(f"Theoretical lambda: {lambda_test}")
print(f"Sample mean: {sample_mean:.4f}")
print(f"Sample variance: {sample_variance:.4f}")