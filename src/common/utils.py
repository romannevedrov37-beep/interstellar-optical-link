"""
Вспомогательные функции: конвертация единиц измерения и логирование.
"""

import logging


def nm_to_m(wavelength_nm: float) -> float:
    """Переводит длину волны из нанометров в метры."""
    return wavelength_nm * 1e-9


def m_to_nm(wavelength_m: float) -> float:
    """Переводит длину волны из метров в нанометры."""
    return wavelength_m * 1e9


def get_logger(name: str) -> logging.Logger:
    """Создаёт простой логгер с заданным именем."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    return logging.getLogger(name)
