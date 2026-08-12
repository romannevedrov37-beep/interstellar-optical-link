"""
Photon rate calculations: converts received optical power into
photon arrival rate, based on photon energy at a given wavelength.
"""
def received_power(P: float, D_t: float, D_r: float, wavelength_m: float, R: float) -> float:
    """Received power at the telescope, given diffraction-limited beam
    divergence theta = wavelength / D_t (no Airy 1.22 factor)."""
    theta = 1.22 * wavelength_m / D_t
    spot_radius = theta * R
    area_ratio = (D_r / 2)**2 / spot_radius**2
    return P * area_ratio
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

