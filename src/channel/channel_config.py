from dataclasses import dataclass
from math import log2


@dataclass
class ChannelConfig:
    """Time-slot configuration for PPM modulation."""
    slot_duration_s: float   #длительность одного слота в секундах
    ppm_order: int           #M — количество слотов в одном PPM-символе

    def bits_per_symbol(self) -> float:
        """Сколько бит кодирует один PPM-символ."""
        return log2(self.ppm_order) 

    def symbol_duration_s(self) -> float:
        """Длительность всего символа (M слотов подряд)."""
        return self.slot_duration_s*self.ppm_order 