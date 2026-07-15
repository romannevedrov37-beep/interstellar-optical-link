import numpy as np


class PPMDecoder:
    """Decodes PPM one-hot symbol frames back into bits."""

    def __init__(self, ppm_order: int):
        self.ppm_order = ppm_order
        self.bits_per_symbol = int(np.log2(ppm_order))

    def decode_symbol(self, frame: np.ndarray) -> list:
        """
        Given a one-hot PPM frame, find the position of the pulse
        and convert it back into a list of bits.
        """
        position = np.argmax(frame) 

        bit_string = format(position, f'0{self.bits_per_symbol}b')

        bits = [int(b) for b in bit_string]
        return bits