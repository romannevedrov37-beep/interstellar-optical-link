"""
Photon efficiency metrics: how many bits are delivered per photon spent.

Two variants are provided:
  - bits_per_photon: raw channel efficiency, ignores errors entirely
  - effective_bits_per_photon: scales by (1 - BER) as a rough proxy

NOTE: the (1 - BER) scaling is a placeholder, not information-theoretically
correct. At BER = 0.5 the receiver is guessing at random and delivers zero
usable information, but (1 - BER) still reports half the bits as "successful".
The correct treatment uses binary-symmetric-channel capacity, C = 1 - H(BER),
where H is the binary entropy function. To be replaced once FEC experiments
begin.
"""


def bits_per_photon(message_bits: int, num_symbols: int, lambda_per_slot: float) -> float:
    """
    Raw channel efficiency: message bits divided by the average number of
    photons consumed transmitting them over `num_symbols` PPM symbols.

    Ignores errors and decoding outcome entirely. Only meaningful in regimes
    where the channel actually works — at very low lambda it returns huge
    values that reflect photon starvation, not efficiency.
    """
    avg_photons_used = lambda_per_slot * num_symbols
    return message_bits / avg_photons_used


def effective_bits_per_photon(message_bits: int, ber: float, num_symbols: int, lambda_per_slot: float) -> float:
    """
    Bits per photon scaled by (1 - BER) as a first-order correction for
    reception errors.

    See module docstring: this scaling is a placeholder and overestimates
    delivered information at high BER.
    """
    successful_bits = message_bits * (1 - ber)
    avg_photons_used = num_symbols * lambda_per_slot
    return successful_bits / avg_photons_used
