import sys
sys.path.append('.')

from src.pipeline.uncoded_pipeline import run_uncoded_pipeline

payload = b"Hi"

recovered = run_uncoded_pipeline(
    payload=payload,
    ppm_order=16,
    lambda_signal=50.0,
    lambda_background=0.05,
    dark_rate=0.001,
    eta=0.9,
    seed=42
)

print(f"Original payload: {payload}")
print(f"Recovered payload: {recovered}")
print(f"Match: {payload == recovered}")