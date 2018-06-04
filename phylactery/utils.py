# =============================================================================
# Phylactery Utilities
# =============================================================================
#
# Miscellaneous functions used throughout the library.
#
import numpy as np

MAX_UINT8 = np.iinfo(np.uint8).max
MAX_UINT16 = np.iinfo(np.uint16).max
MAX_UINT32 = np.iinfo(np.uint32).max


def get_minimal_dtype_for_capacity(capacity):
    """
    Function returning the minimum numpy integer dtype to store zero-based
    indices needing to store the desired capacity.

    Args:
        capacity (number): Desired capacity.

    """
    max_index = capacity - 1

    if max_index <= MAX_UINT8:
        return np.uint8

    if max_index <= MAX_UINT16:
        return np.uint16

    if max_index <= MAX_UINT32:
        return np.uint32

    return np.uint64
