import pytest
from src.channel.photon_rate import photons_per_second, photons_per_slot

import sys
sys.path.append('.')

from src.channel.photon_rate import photon_energy, photons_per_second, photons_per_slot

def test_photons_per_second_known_value():
    """Check photon rate against a hand-computed reference value."""
    received_power_w = 3.910374995739635e-15
    wavelength_m = 1550e-9
    result = photons_per_second(received_power_w, wavelength_m)
    assert abs(result - 30512.19) < 0.01


def test_photons_per_slot_known_value():
    """Check photons-per-slot against a hand-computed reference value."""
    photon_rate = 30512.189504604357
    slot_duration_s = 1e-9
    result = photons_per_slot(photon_rate, slot_duration_s)
    assert abs(result - 3.0512e-05) < 1e-8
    