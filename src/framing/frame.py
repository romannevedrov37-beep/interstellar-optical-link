SYNC_BYTE = 0xAA


def build_frame(payload: bytes) -> bytes:
    """Wrap payload in a frame: SYNC + LENGTH + PAYLOAD + CHECKSUM."""
    length = len(payload)
    length_bytes = length.to_bytes(2, byteorder='big')
    checksum = sum(payload) % 256

    frame = bytes([SYNC_BYTE]) + length_bytes + payload + bytes([checksum])
    return frame

def parse_frame(frame: bytes) -> bytes:
    if frame[0] != SYNC_BYTE:
        raise ValueError("some description")
    length = int.from_bytes(frame[1:3], byteorder='big')
    payload = frame[3:3+length]
    checksum = sum(payload) % 256
    if checksum != frame[-1]:
       raise ValueError("some description")
    return payload