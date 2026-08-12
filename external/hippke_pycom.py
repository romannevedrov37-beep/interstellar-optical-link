"""
Vendored from hippke/communication (PyCom.py), MIT License.
Source: https://github.com/hippke/communication
Author: Michael Hippke
Only the photons_received() function is used here; the rest of PyCom.py
(gravitational lensing, Holevo capacity) is out of scope for this project.
"""
from astropy.constants import c
from astropy import units as u
from math import pi

def photons_received(D_r, D_t, P, wavelength, R, Q_R=1.22):
    """Number of photons that telescope with aperture D_r [m] receives,
    D_t [m] aperture of transmitting telescope,
    wavelength lambda in [m],
    R [m] distance between D_r and D_t
    Q_R [1] diffraction limit"""
    h = 6.62607004E-34
    f = 1 / (wavelength / c) / (u.meter / u.second)
    F_r = P / ((pi * h * f) * (Q_R * wavelength / D_t * R)**2) * pi * D_r**2 / 4
    return F_r
