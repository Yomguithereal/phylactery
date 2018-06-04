# =============================================================================
# Phylactery BitSet
# =============================================================================
#
# A simple Python BitSet implementation relying on Numpy.
#
import math
import numpy as np

MODULO = 0x0000001f


class BitSet(object):
    """
    The BitSet class.

    Args:
        capacity (number): Capacity of the bitset.

    """

    def __init__(self, capacity):
        true_capacity = math.ceil(capacity / 32)

        # Properties
        self.capacity = capacity
        self.__integers = np.zeros(true_capacity, dtype=np.uint32)

    def __len__(self):
        return self.capacity

    def get(self, index):

        if index >= self.capacity:
            raise IndexError

        byte = index >> 5
        pos = index & MODULO

        return (self.__integers[byte] >> pos) & 1

    def has(self, index):
        return self.get(index) == 1

    def test(self, index):
        return self.has(index)

    def set(self, index, value=1):
        if index >= self.capacity:
            raise IndexError

        byte = index >> 5
        pos = index & MODULO

        if not value:
            self.__integers[byte] &= ~(1 << pos)
        else:
            self.__integers[byte] |= (1 << pos)

    def reset(self, index):
        if index >= self.capacity:
            raise IndexError

        byte = index >> 5
        pos = index & MODULO

        self.__integers[byte] &= ~(1 << pos)

    def add(self, index):
        return self.set(index)

    def __getitem__(self, index):
        return self.get(index)

    def __contains__(self, index):
        return self.has(index)

    def __setitem__(self, index, value):
        return self.set(index, value)

    def __delitem__(self, index):
        return self.reset(index)

    def __repr__(self):
        return '<%s capacity=%i>' % (self.__class__.__name__, self.capacity)
