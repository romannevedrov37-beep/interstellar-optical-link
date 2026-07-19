import sys
sys.path.append('.')

import pandas as pd
from src.experiments.uncoded_sweep import run_trial

lambda_signal_values = [0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]

results = []

for lam in lambda_signal_values:
    result = run_trial(
        lambda_signal=lam,
        lambda_background=0.05,
        dark_rate=0.001,
        eta=0.9,
        ppm_order=16,
        num_bits=256,
        seed=42
    )
    results.append(result)

df = pd.DataFrame(results)
print(df)

df.to_csv("results/uncoded_baseline.csv", index=False)