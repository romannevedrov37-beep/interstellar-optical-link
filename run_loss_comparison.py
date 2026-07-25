import sys

sys.path.append('.')

from src.experiments.uncoded_sweep import run_trial_with_erasures, run_trial_with_burst
import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
bits = rng.integers(0, 2, size=256).tolist()
loss_rate = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25]
results = []
for rate in loss_rate:
    lid = run_trial_with_erasures(bits=bits, ppm_order=16, erasure_rate=rate, seed=42)
    burst = run_trial_with_burst(bits=bits, ppm_order=16, loss_rate=rate, seed=42)
    ber_iid = lid["ber"]
    ber_burst = burst["ber"]
    ser_iid = lid["ser"]
    ser_burst = burst["ser"]
    results.append({"loss_rate": rate, "ber_iid": ber_iid, "ber_burst": ber_burst, "ser_iid": ser_iid, "ser_burst": ser_burst})
df = pd.DataFrame(results)
df.to_csv("results/no_fec_burst.csv", index=False)
print(df)