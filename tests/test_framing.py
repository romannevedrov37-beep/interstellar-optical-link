import sys
sys.path.append('.')

from src.framing.frame import build_frame, parse_frame
payload = b"Hello"
frame = build_frame(payload)
print(frame)
recovered = parse_frame(frame)
print (recovered)
print (payload == recovered)