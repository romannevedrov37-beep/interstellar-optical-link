from src.common.constants import SPEED_OF_LIGHT, PLANCK_CONSTANT, DEFAULT_WAVELENGTH_M
from src.common.utils import nm_to_m, m_to_nm, get_logger

logger = get_logger("test_constants")

logger.info(f"Скорость света: {SPEED_OF_LIGHT} м/с")
logger.info(f"Постоянная Планка: {PLANCK_CONSTANT} Дж·с")
logger.info(f"Длина волны по умолчанию: {DEFAULT_WAVELENGTH_M} м")

# Проверка конвертации
wavelength_nm = 1550
wavelength_m = nm_to_m(wavelength_nm)
back_to_nm = m_to_nm(wavelength_m)

logger.info(f"{wavelength_nm} нм = {wavelength_m} м")
logger.info(f"Обратно: {wavelength_m} м = {back_to_nm} нм")

assert abs(back_to_nm - wavelength_nm) < 1e-6, "Ошибка конвертации туда-обратно!"
logger.info("Все проверки пройдены успешно")