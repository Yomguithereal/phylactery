# =============================================================================
# Phylactery Utils Unit Tests
# =============================================================================
import numpy as np
import pytest
from phylactery.utils import get_minimal_dtype_for_capacity

TESTS = [
    (256, np.uint8),
    (345, np.uint16),
    (453672, np.uint32),
    (976397596390065, np.uint64)
]


class TestBitSet(object):
    def test_get_minimal_dtype_for_capacity(self):

        for capacity, dtype in TESTS:
            assert get_minimal_dtype_for_capacity(capacity) is dtype
