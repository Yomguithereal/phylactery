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

COMPONENTS = [
    [3, 4],
    [5],
    [0, 1, 2, 6]
]


class TestBitSet(object):
    def test_basics(self):
        sets = UnionFind(7)

        for A, B in EDGES:
            sets.union(A, B)

        assert sets.capacity == 7
        assert sets.components == 4

        sets.union(6, 1)

        assert sets.components == 3

        for i, component in enumerate(sets):
            assert list(component) == COMPONENTS[i]
