def bit_error_count(bits_sent: list, bits_received: list) -> int:
    """Count the number of differing bits between sent and received."""
    counter = 0
    for i in range(len(bits_sent)):
        if bits_sent[i] != bits_received[i]:
            counter += 1
    return counter
def bit_error_rate(bits_sent: list, bits_received: list) -> float:
    """Fraction of bits that differ between sent and received."""
    errors = bit_error_count(bits_sent, bits_received) 
    total = len(bits_sent)
    return errors / total

def symbol_error_rate(bits_sent: list, bits_received: list, bits_per_symbol: int) -> float:
    """Fraction of symbols where at least one bit differs."""
    num_symbols = len(bits_sent)// bits_per_symbol
    error_counter = 0
    for s in range(num_symbols):
        start = s * bits_per_symbol
        end = start + bits_per_symbol
        symbol_sent = bits_sent[start: end]
        symbol_received = bits_received[start: end]
        if symbol_sent != symbol_received:
           error_counter += 1
    return error_counter / num_symbols

def recovery_success(bits_sent: list, bits_received: list) -> bool:
    """True if the entire message was recovered exactly, False otherwise."""
    return bits_sent == bits_received
