"""
Photon rate calculations: converts received optical power into
photon arrival rate, based on photon energy at a given wavelength.
"""
def received_power(P: float, D_t: float, D_r: float, wavelength_m: float, R: float) -> float:
    """Received power at the telescope, given diffraction-limited beam
divergence theta = 1.22 * wavelength / D_t (Airy disk, circular aperture)."""
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
if __name__ == "__main__":
    wavelength_m = 1550e-9
    P = 1e9
    D_t = 0.3
    D_r = 1.0
    R = 4.0113497203742592e16

    power = received_power(P, D_t, D_r, wavelength_m, R)
    rate = photons_per_second(power, wavelength_m)
    slot_duration_s = 1e-9
    per_slot = photons_per_slot(rate, slot_duration_s)

    print(f"Received power: {power}")
    print(f"Photons per second: {rate}")
    print(f"Photons per slot: {per_slot}")
    

