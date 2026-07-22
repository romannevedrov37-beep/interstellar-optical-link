import sys
sys.path.append('.')

from src.channel.burst_model import generate_burst_mask
mask = generate_burst_mask(num_symbols=20, burst_length=3, seed=1)
print(mask)
print(sum(mask))