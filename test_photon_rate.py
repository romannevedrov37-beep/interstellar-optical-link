import sys
sys.path.append('.')

from src.channel.photon_rate import photon_energy, photons_per_second, photons_per_slot

wavelength_m = 1550e-9
received_power_w = 5.82e-15

print(f"Photon energy: {photon_energy(wavelength_m):.3e} J")
print(f"Photons per second: {photons_per_second(received_power_w, wavelength_m):.3e}")

rate = photons_per_second(received_power_w, wavelength_m)
slot_duration_s = 1e-9   
per_slot = photons_per_slot(rate, slot_duration_s)
print(f"Photons per slot: {per_slot:.3e}")