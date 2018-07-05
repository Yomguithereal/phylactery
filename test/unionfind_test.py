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
    [5],
    [3, 4],
    [0, 1, 2, 6]
]


class TestBitSet(object):
    def test_basics(self):
        sets = UnionFind(7)

        for A, B in EDGES:
            sets.union(A, B)

        assert sets.capacity == 7
        assert sets.count == 4

        assert sets.connected(1, 2)
        assert not sets.connected(4, 6)

        sets.union(6, 1)

        assert sets.count == 3

        assert sorted(sets, key=len) == COMPONENTS

        small_components = sorted(sets.components(max_size=2), key=len)

        assert small_components == COMPONENTS[:2]

        large_components = sorted(sets.components(min_size=3), key=len)

        assert large_components == COMPONENTS[2:]
