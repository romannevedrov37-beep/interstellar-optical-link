import numpy as np
from src.modem.ppm_encoder import PPMEncoder
from src.modem.ppm_decoder import PPMDecoder
from src.channel.poisson_channel import sample_photon_counts
from src.detector.snspd_model import SNSPDDetector
from src.metrics.metrics import bit_error_rate, symbol_error_rate, recovery_success


def run_trial(lambda_signal, lambda_background, dark_rate, eta, ppm_order, num_bits, seed):
    encoder = PPMEncoder(ppm_order=ppm_order)
    decoder = PPMDecoder(ppm_order=ppm_order)
    detector = SNSPDDetector(eta=eta, dark_rate=dark_rate)

    decoded_bits = []
    rng_seed = seed
    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, size=num_bits).tolist()
    bits_per_symbol = encoder.bits_per_symbol
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
    ber = bit_error_rate(bits, decoded_bits)
    ser =symbol_error_rate(bits, decoded_bits, bits_per_symbol)
    success = recovery_success(bits, decoded_bits)
    return {"lambda_signal": lambda_signal, "ber": ber, "ser": ser, "success": success}
