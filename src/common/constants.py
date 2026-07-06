"""
Physical constants and project parameters.
Values are taken from scipy.constants to avoid having to enter them manually
and to prevent errors in the order of magnitude.
"""

from scipy import constants

SPEED_OF_LIGHT = constants.c
PLANCK_CONSTANT = constants.h
DEFAULT_WAVELENGTH_M = 1550e-9
