import sys
sys.path.append('.')

from src.modem.ppm_encoder import PPMEncoder

encoder = PPMEncoder(ppm_order=16)
print(f"Bits per symbol: {encoder.bits_per_symbol}")

frame = encoder.encode_symbol([1, 0, 1, 0])
print(f"Encoded frame: {frame}")