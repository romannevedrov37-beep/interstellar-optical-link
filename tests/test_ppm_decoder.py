import sys
sys.path.append('.')

from src.modem.ppm_encoder import PPMEncoder
from src.modem.ppm_decoder import PPMDecoder

encoder = PPMEncoder(ppm_order=16)
decoder = PPMDecoder(ppm_order=16)

original_bits = [1, 0, 1, 0]
frame = encoder.encode_symbol(original_bits)
decoded_bits = decoder.decode_symbol(frame)

print(f"Original bits: {original_bits}")
print(f"Encoded frame: {frame}")
print(f"Decoded bits: {decoded_bits}")
print(f"Round-trip successful: {original_bits == decoded_bits}")