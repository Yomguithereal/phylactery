# =============================================================================
# Phylactery Union Find
# =============================================================================
#
# A static Union Find data structure useful to find disjoint sets and
# connected components.
#
import math
import numpy as np
from phylactery.utils import get_minimal_dtype_for_capacity


class UnionFind(object):
    """
    The UnionFind class.

    Args:
        capacity (number): total number of items to store.

    """

    def __init__(self, capacity):

        parents_dtype = get_minimal_dtype_for_capacity(capacity)
        ranks_dtype = get_minimal_dtype_for_capacity(math.log2(capacity))

        # Properties
        self.capacity = capacity
        self.components = capacity
        self.parents = np.arange(capacity, dtype=parents_dtype)
        self.ranks = np.zeros(capacity)

    def __len__(self):
        return self.capacity

    def find(self, x):
        y = x
        parents = self.parents

        while True:
            c = parents[y]

            if y == c:
                break

            y = c

        # Path compression
        while True:
            p = parents[x]

            if p == y:
                break

            x = p

        return y

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        parents = self.parents
        ranks = self.ranks

        # x & y are already in the same set
        if x_root == y_root:
            return

        self.components -= 1

        # x & y are not in the same set, we merge them
        x_rank = ranks[x]
        y_rank = ranks[y]

        if x_rank < y_rank:
            parents[x_root] = y_root
        elif x_rank > y_rank:
            parents[y_root] = x_root
        else:
            parents[y_root] = x_root
            ranks[x_root] += 1

    def __getitem__(self, x):
        return self.find(x)

    def __repr__(self):
        return '<%s capacity=%i components=%i>' % (
            self.__class__.__name__,
            self.capacity,
            self.components
        )
