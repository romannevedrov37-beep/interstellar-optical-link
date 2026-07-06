“”"
Utility functions: unit conversion and logging.
“”"

import logging


def nm_to_m(wavelength_nm: float) -> float:
    “”“Converts a wavelength from nanometers to meters.”“”
    return wavelength_nm * 1e-9


def m_to_nm(wavelength_m: float) -> float:
    “”“Converts wavelength from meters to nanometers.”“”
    return wavelength_m * 1e9


def get_logger(name: str) -> logging.Logger:
    “”“Creates a simple logger with the specified name.”" "
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    return logging.getLogger(name)
