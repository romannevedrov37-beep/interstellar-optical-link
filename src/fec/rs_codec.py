"""
Reed-Solomon codec wrapper over the reedsolo library.
Operates on byte-level symbols in GF(2^8).
"""
from reedsolo import RSCodec

class RSCodecWrapper:
    def __init__(self, nsym: int = 32):
        self.rs_codec = RSCodec(nsym)
        self.nsym = nsym

    def encode(self, data: bytes) -> bytes:
        if len(data) > 255 - self.nsym:
            raise ValueError(f"Payload too long: {len(data)} bytes, max is {255 - self.nsym}")
        return self.rs_codec.encode(data)

    def decode(self, codeword: bytes) -> bytes:
        return self.rs_codec.decode(codeword)[0]


if __name__ == "__main__":
    codec = RSCodecWrapper()
    nsym=10
    original = b"Hello"
    encoded = codec.encode(original)
    decoded = codec.decode(encoded)
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {decoded == original}")
        