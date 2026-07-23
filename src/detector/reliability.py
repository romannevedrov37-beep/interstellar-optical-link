import numpy as np


def classify_symbol(frame: np.ndarray, margin_threshold: int) -> tuple:
    """
    Classify a PPM symbol as reliable or erased, based on the margin
    between the top slot count and the second-highest slot count.
    Returns (position, is_erasure).
    """
    position = np.argmax(frame)
    sorted_frame = np.sort(frame)
    margin =  sorted_frame[-1] - sorted_frame[-2] 
    if margin < margin_threshold:
        is_erasure = True
    else:
        is_erasure = False
    return position, is_erasure