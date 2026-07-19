import sys
sys.path.append('.')

from src.experiments.uncoded_sweep import run_trial

result = run_trial(
    lambda_signal=10,
    lambda_background=0.05,
    dark_rate=0.001,
    eta=0.9,
    ppm_order=16,
    num_bits=64,
    seed=42
)

print(result)