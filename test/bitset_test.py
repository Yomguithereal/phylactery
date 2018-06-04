# =============================================================================
# Phylactery BitSet Unit Tests
# =============================================================================
import pytest
from phylactery import BitSet


class TestBitSet(object):
    def test_basics(self):
        bitset = BitSet(4)

        assert bitset.capacity == 4
        assert len(bitset) == 4

        assert bitset.get(2) == 0
        assert bitset.get(1) == 0

        with pytest.raises(IndexError):
            bitset.get(34)

        assert bitset[0] == 0
        assert bitset[1] == 0

        bitset.set(0)
        bitset.set(1, True)
        bitset.set(3, False)

        assert bitset[0] == 1
        assert bitset[1] == 1
        assert bitset[3] == 0

        assert bitset.test(0)
        assert bitset.has(1)
        assert 1 in bitset

        bitset[2] = True

        assert 2 in bitset

        bitset.reset(2)

        assert 2 not in bitset

        del bitset[0]

        assert bitset.get(0) == 0

        with pytest.raises(IndexError):
            bitset.add(5)

        bitset.add(0)

        assert 0 in bitset

        bitset = BitSet(4)

        bitset.update((i for i in [2, 3]))

        assert 0 not in bitset
        assert 1 not in bitset
        assert 2 in bitset
        assert 3 in bitset
