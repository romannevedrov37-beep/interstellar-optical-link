import sys
sys.path.append('.')

import pandas as pd
from src.experiments.uncoded_sweep import run_trial

lambda_signal_values = [3.05e-5, 1e-4, 1e-3, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]

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

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(df["lambda_signal"], df["ber"], 'o-', label="BER")
plt.plot(df["lambda_signal"], df["ser"], 's-', label="SER")
plt.xscale('log')
plt.xlabel("lambda_signal (log scale)")
plt.ylabel("Error rate")
plt.title("Uncoded baseline: BER and SER vs signal strength")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("figures/uncoded_baseline_ber_ser.png")
plt.show()

plt.figure(figsize=(8, 5))
success_numeric = df["success"].astype(int)
plt.plot(df["lambda_signal"], success_numeric, 'o-', color='green')
plt.xscale('log')
plt.xlabel("lambda_signal (log scale)")
plt.ylabel("Recovery success (1=True, 0=False)")
plt.title("Uncoded baseline: message recovery success vs signal strength")
plt.grid(True, alpha=0.3)
plt.savefig("figures/uncoded_baseline_success.png")
plt.show()
