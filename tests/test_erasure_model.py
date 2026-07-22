import sys
sys.path.append('.')

from src.channel.erasure_model import generate_erasure_mask

mask = generate_erasure_mask(num_symbols=20, erasure_rate=0.25, seed=42)
print(mask)
print(sum(mask))
