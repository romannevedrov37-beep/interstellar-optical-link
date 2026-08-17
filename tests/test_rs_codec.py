from math import floor
import pytest
from src.fec.rs_codec import RSCodecWrapper
from reedsolo import ReedSolomonError

codec = RSCodecWrapper(nsym=10)
original = b"Hello"
encoded = codec.encode(original)
def test_round_trip_no_corruption():
    """Encode then decode with zero corruption should return the exact original."""
    decoded = codec.decode(encoded)
    assert decoded == original

def test_encode_adds_parity_length():
    """Encoded length should equal original length + nsym."""
    nsym=10
    assert len(encoded) == len(original) + nsym

def test_decode_recovers_within_capacity():
    """Corrupting up to floor(nsym/2) symbols (unknown errors) should still decode correctly."""
    nsym = 10
    errors_to_inject = floor(nsym / 2)
    corrupted = bytearray(encoded)
    for i in range(errors_to_inject):
        corrupted[i] ^= 0xFF
    decoded = codec.decode(corrupted)
    is_same = (original == decoded)
    assert is_same
def test_decode_fails_beyond_capacity():
    """Corrupting more than floor(nsym/2) symbols should raise ReedSolomonError."""
    nsym = 10
    corrupted = bytearray(encoded)
    errors_to_inject = floor(nsym / 2) + 1
    for i in range(errors_to_inject):
        corrupted[i] ^= 0xFF  
    with pytest.raises(ReedSolomonError):
        codec.decode(corrupted)
        
        
        
        