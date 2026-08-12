"""
Cross-validation: my photon rate model vs. Hippke's PyCom.photons_received().
"""
import sys
sys.path.append('.')

from external.hippke_pycom import photons_received
from src.channel.photon_rate import received_power, photons_per_second

# Общие параметры (из docs/model_assumptions.md)
D_r = 1.0        # приёмный телескоп, м
D_t = 0.3        # передающая апертура, м
P = 1e9          # мощность лазера, Вт
wavelength = 1.55e-6  # м
R = 4.01e16      # м

my_power = received_power(P, D_t, D_r, wavelength, R)
my_result = photons_per_second(my_power, wavelength)

hippke_result = photons_received(D_r, D_t, P, wavelength, R)
discrepancy = (my_result - hippke_result) / hippke_result

print(f"My result: {my_result}")
print(f"PyCom result: {hippke_result}")
print(f"Discrepancy: {discrepancy}")
