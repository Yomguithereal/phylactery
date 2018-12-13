# =============================================================================
# Phylactery BitSet
# =============================================================================
#
# A simple Python BitSet implementation. It seems it remains slower than a
# cpython set which is a tad disappointing to say the least.
#
import math

MODULO = 0x0000001f


class BitSet(object):
    """
    The BitSet class.

    Args:
        capacity (number): Capacity of the bitset.

    """

    __slots__ = ('capacity', 'integers')

    def __init__(self, capacity):
        true_capacity = math.ceil(capacity / 32)

        # Properties
        self.capacity = capacity
        self.integers = [0] * true_capacity

    def __len__(self):
        return self.capacity

    def get(self, index):

        if index >= self.capacity:
            raise IndexError

        byte = index >> 5
        pos = index & MODULO

        return (self.integers[byte] >> pos) & 1

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
            self.integers[byte] &= ~(1 << pos)
        else:
            self.integers[byte] |= (1 << pos)

    def update(self, iterable):
        for index in iterable:
            self.set(index)

    def reset(self, index):
        if index >= self.capacity:
            raise IndexError

        byte = index >> 5
        pos = index & MODULO

        self.integers[byte] &= ~(1 << pos)

    def add(self, index):
        return self.set(index)

    def delete(self, index):
        return self.reset(index)

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
