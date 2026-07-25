import numpy as np
from src.channel.burst_model import generate_burst_mask
from src.channel.erasure_model import generate_erasure_mask
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

from src.channel.erasure_model import generate_erasure_mask
def run_trial_with_erasures(bits, ppm_order, erasure_rate, seed):
    """
    Encode bits into PPM symbols, apply an iid erasure mask directly
    (bypassing the photon channel), and measure recovery metrics.
    Erased symbols are treated as fully lost (all bits wrong).
    """
    encoder = PPMEncoder(ppm_order=ppm_order)
    decoder = PPMDecoder(ppm_order=ppm_order)
    bits_per_symbol = encoder.bits_per_symbol
    symbol_groups = []
    for i in range(0, len(bits), bits_per_symbol):
        symbol_bits = bits[i:i+bits_per_symbol]
        symbol_groups.append(symbol_bits)
    num_symbols = len(symbol_groups)
    erasure_mask = generate_erasure_mask(num_symbols=num_symbols, erasure_rate=erasure_rate, seed=seed)
    decoded_bits = []
    for symbol_bits, is_erased in zip(symbol_groups, erasure_mask):
        if is_erased:
            decoded_bits.extend(1 - bit for bit in symbol_bits)
        else:
            frame = encoder.encode_symbol(symbol_bits)
            decoded_symbol_bits = decoder.decode_symbol(frame)
            decoded_bits.extend(decoded_symbol_bits)
    ber = bit_error_rate(bits,decoded_bits)
    ser = symbol_error_rate(bits,decoded_bits,bits_per_symbol)
    success = recovery_success(bits,decoded_bits)
    return {"erasure_rate": erasure_rate, "ber": ber, "ser": ser, "success": success}

def run_trial_with_burst(bits, ppm_order, loss_rate, seed):
    """
    Same as run_trial_with_erasures, but losses are contiguous (one burst)
    instead of iid. loss_rate is converted into a burst length so that both
    models can be compared on the same total-loss axis.
    """
    encoder = PPMEncoder(ppm_order=ppm_order)
    decoder = PPMDecoder(ppm_order=ppm_order)
    bits_per_symbol = encoder.bits_per_symbol
    symbol_groups = []
    decoded_bits = []
    for i in range(0, len(bits), bits_per_symbol):
        symbol_bits = bits[i:i+bits_per_symbol]
        symbol_groups.append(symbol_bits)
    num_symbols = len(symbol_groups)
    burst_length = int(num_symbols * loss_rate)
    erasure_mask = generate_burst_mask(num_symbols=num_symbols, burst_length=burst_length, seed=seed)
    for symbol_bits, is_erased in zip(symbol_groups, erasure_mask):
            if is_erased:
                decoded_bits.extend(1 - bit for bit in symbol_bits)
            else:
                frame = encoder.encode_symbol(symbol_bits)
                decoded_symbol_bits = decoder.decode_symbol(frame)
                decoded_bits.extend(decoded_symbol_bits)
    ber = bit_error_rate(bits,decoded_bits)
    ser = symbol_error_rate(bits,decoded_bits,bits_per_symbol)
    success = recovery_success(bits,decoded_bits)
    return {"loss_rate": loss_rate, "ber": ber, "ser": ser, "success": success}
