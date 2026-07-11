import sys
sys.path.append('.')

from src.channel.poisson_channel import sample_photon_counts

lambda_signal = 0.5
lambda_background = 0.05

pulsed_counts = sample_photon_counts(lambda_signal + lambda_background, size=10, seed=42)
unpulsed_counts = sample_photon_counts(lambda_background, size=10, seed=42)

print(f"Pulsed slot counts: {pulsed_counts}")
print(f"Unpulsed slot counts: {unpulsed_counts}")