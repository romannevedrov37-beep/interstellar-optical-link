def bytes_to_bits(data: bytes) -> list:
    """Convert bytes into a flat list of 0/1 bits."""
    bits = []
    for byte in data:
     for i in range(7, -1, -1):
        bits.append((byte >> i) & 1)
    return bits

if __name__ == "__main__":
    result = bytes_to_bits(b"Hi")
    print(result)

def bits_to_bytes(bits: list) -> bytes:
    """Convert a flat list of 0/1 bits back into bytes."""
    byte_values = []
    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        value = 0
        for bit in chunk:
            value = (value << 1) | bit
        byte_values.append(value)
    return bytes(byte_values)
import numpy as np
from src.modem.ppm_encoder import PPMEncoder
from src.modem.ppm_decoder import PPMDecoder
from src.channel.poisson_channel import sample_photon_counts
from src.detector.snspd_model import SNSPDDetector
def run_uncoded_pipeline(payload, ppm_order, lambda_signal, lambda_background, dark_rate, eta, seed=42):
    encoder = PPMEncoder(ppm_order=ppm_order)
    decoder = PPMDecoder(ppm_order=ppm_order)
    detector = SNSPDDetector(eta=eta, dark_rate=dark_rate)

    bits = bytes_to_bits(payload)
    bits_per_symbol = encoder.bits_per_symbol

    padding = (-len(bits)) % bits_per_symbol
    bits = bits + [0] * padding

    decoded_bits = []
    rng_seed = seed

    for i in range(0, len(bits), bits_per_symbol):
        symbol_bits = bits[i:i+bits_per_symbol]
        frame = encoder.encode_symbol(symbol_bits)

        true_counts = np.zeros(ppm_order, dtype=int)
        for slot_idx in range(ppm_order):
            pulsed = frame[slot_idx] == 1
            lam = (lambda_signal + lambda_background) if pulsed else lambda_background
            true_counts[slot_idx] = sample_photon_counts(lam, size=1, seed=rng_seed + slot_idx)[0]

        observed = detector.observe(true_counts, seed=rng_seed)
        decoded_symbol_bits = decoder.decode_symbol(observed)
        decoded_bits.extend(decoded_symbol_bits)

        rng_seed += 1

    decoded_bits = decoded_bits[:len(bits) - padding]
    return bits_to_bytes(decoded_bits)

if __name__ == "__main__":
    bits = bytes_to_bits(b"Hi")
    print(f"Bits: {bits}")

    recovered = bits_to_bytes(bits)
    print(f"Recovered bytes: {recovered}")
    print(f"Match: {recovered == b'Hi'}")