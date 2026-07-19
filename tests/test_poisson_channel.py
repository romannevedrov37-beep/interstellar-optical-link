import sys
sys.path.append('.')

from src.channel.poisson_channel import sample_photon_counts

lambda_signal = 0.5
lambda_background = 0.05

pulsed_counts = sample_photon_counts(lambda_signal + lambda_background, size=10, seed=42)
unpulsed_counts = sample_photon_counts(lambda_background, size=10, seed=42)

print(f"Pulsed slot counts: {pulsed_counts}")
print(f"Unpulsed slot counts: {unpulsed_counts}")

from src.channel.poisson_channel import sample_photon_counts, combined_lambda

dark_count_rate = 0.001  

pulsed_lambda = combined_lambda(lambda_signal, lambda_background, dark_count_rate, pulsed=True)
unpulsed_lambda = combined_lambda(lambda_signal, lambda_background, dark_count_rate, pulsed=False)

print(f"Pulsed lambda: {pulsed_lambda}")
print(f"Unpulsed lambda: {unpulsed_lambda}")

pulsed_counts_v2 = sample_photon_counts(pulsed_lambda, size=10, seed=42)
unpulsed_counts_v2 = sample_photon_counts(unpulsed_lambda, size=10, seed=42)

print(f"Pulsed slot counts (with dark counts): {pulsed_counts_v2}")
print(f"Unpulsed slot counts (with dark counts): {unpulsed_counts_v2}")