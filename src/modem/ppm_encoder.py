import numpy as np


class PPMEncoder:
    """Encodes groups of bits into PPM one-hot symbol frames."""

    def __init__(self, ppm_order: int):
        self.ppm_order = ppm_order
        self.bits_per_symbol = int(np.log2(ppm_order))

    def encode_symbol(self, bits: list) -> np.ndarray:
        """
        Convert a list of bits (e.g. [1, 0, 1, 0]) into a one-hot
        PPM frame of length ppm_order, with a single 1 at the
        position corresponding to the binary value of the bits.
        """
        bit_string = "".join(str(b) for b in bits)
        position = int(bit_string, 2)   
        frame = np.zeros(self.ppm_order)
        frame[position] = 1  

        return frame