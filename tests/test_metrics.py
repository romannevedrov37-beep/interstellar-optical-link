import sys
sys.path.append('.')

from src.metrics.metrics import bit_error_count, bit_error_rate, symbol_error_rate, recovery_success

bits_sent = [1, 0, 1, 1, 0]
bits_received = [1, 1, 1, 0, 0]

errors = bit_error_count(bits_sent, bits_received)
rate = bit_error_rate(bits_sent, bits_received)

print(f"Errors: {errors}")
print(f"BER: {rate}")

bits_sent_test = [1, 0, 1, 0, 1, 1, 0, 0]
bits_received_test = [1, 0, 1, 0, 1, 0, 0, 0]

ser = symbol_error_rate(bits_sent_test, bits_received_test, bits_per_symbol=4)
print(f"SER: {ser}")

success_1 = recovery_success(bits_sent, bits_received)   # первый пример с BER (там были ошибки)
success_2 = recovery_success(bits_sent_test, bits_received_test)  # второй пример с SER (тоже были ошибки)

print(f"Recovery success (example 1): {success_1}")
print(f"Recovery success (example 2): {success_2}")