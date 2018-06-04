# =============================================================================
# Phylactery UnionFind Unit Tests
# =============================================================================
import pytest
from phylactery import UnionFind

EDGES = [
    (0, 1),
    (1, 2),
    (0, 2),
    (3, 4)
]


class TestBitSet(object):
    def test_basics(self):
        sets = UnionFind(7)

        for A, B in EDGES:
            sets.union(A, B)

        assert sets.capacity == 7
        assert sets.components == 4
