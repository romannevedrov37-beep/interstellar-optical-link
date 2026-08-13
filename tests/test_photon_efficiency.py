import math
from src.metrics.photon_efficiency import bits_per_photon, effective_bits_per_photon


def test_raw_efficiency_basic_arithmetic():
    result = bits_per_photon(message_bits=256, num_symbols=64, lambda_per_slot=10.0)
    assert abs(result - 0.4) < 1e-9


def test_raw_efficiency_ignores_photon_starvation():
    result = bits_per_photon(message_bits=256, num_symbols=64, lambda_per_slot=3.05e-5)
    assert result > 1000
    


def test_effective_equals_raw_when_no_errors():
    raw = bits_per_photon(256, 64, 10.0)
    eff = effective_bits_per_photon(256, 0.0, 64, 10.0)
    print(f"\nРАСЧЕТ: raw={raw}, eff={eff}")
    assert abs(raw - eff) < 1e-9


def test_effective_decreases_as_ber_grows():
    good = effective_bits_per_photon(256, 0.01, 64, 5.0)
    bad = effective_bits_per_photon(256, 0.4, 64, 5.0)
    assert good > bad


def test_known_limitation_at_random_guessing():
    result = effective_bits_per_photon(256, 0.5, 64, 10.0)
    assert abs(result - 0.2) < 1e-9 
    
    
    