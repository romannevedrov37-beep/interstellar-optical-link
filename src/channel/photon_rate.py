"""
Photon rate calculations: converts received optical power into
photon arrival rate, based on photon energy at a given wavelength.
"""
from src.common.constants import PLANCK_CONSTANT, SPEED_OF_LIGHT
def photon_energy(wavelength_m: float) -> float:
    """Energy of a single photon at the given wavelength (Joules)"""
    energy = PLANCK_CONSTANT * SPEED_OF_LIGHT/wavelength_m 
    return energy

def photons_per_second(received_power_w: float, wavelength_m: float) -> float:
    """Average number of photons arriving per second"""
    energy = photon_energy(wavelength_m)
    return received_power_w / energy

def photons_per_slot(photon_rate: float, slot_duration_s: float) -> float:
    """Average number of photons arriving per time slot."""
    return photon_rate * slot_duration_s