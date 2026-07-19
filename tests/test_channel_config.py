import sys
sys.path.append('.')

from src.channel.channel_config import ChannelConfig

config = ChannelConfig(slot_duration_s=1e-9, ppm_order=16)

print(f"Bits per symbol: {config.bits_per_symbol()}")
print(f"Symbol duration: {config.symbol_duration_s():.3e} s")

import sys
sys.path.append('.')

from src.channel.channel_config import ChannelConfig

config = ChannelConfig(slot_duration_s=1e-9, ppm_order=4)

print(f"Bits per symbol: {config.bits_per_symbol()}")
print(f"Symbol duration: {config.symbol_duration_s():.3e} s")