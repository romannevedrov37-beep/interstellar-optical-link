import numpy as np
import sys
sys.path.append('.')
from src.detector.reliability import classify_symbol

frame_a = np.array([0, 5, 0, 0, 0, 0, 0, 0])
frame_b = np.array([0, 2, 0, 1, 0, 0, 0, 0])
print (classify_symbol(frame_a, margin_threshold=2))
print (classify_symbol(frame_b, margin_threshold=2))