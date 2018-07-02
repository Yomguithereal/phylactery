# =============================================================================
# Phylactery Union Find
# =============================================================================
#
# A static Union Find data structure useful to find disjoint sets and
# connected components.
#
import math


class UnionFind(object):
    """
    The UnionFind class.

    Args:
        capacity (number): total number of items to store.

    """

    __slots__ = ('capacity', 'cardinalities', 'count', 'parents', 'ranks')

    def __init__(self, capacity):

        # Properties
        self.capacity = capacity
        self.count = capacity
        self.parents = list(range(capacity))
        self.cardinalities = [1] * capacity
        self.ranks = [0] * capacity

    def __len__(self):
        return self.count

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
        cardinalities = self.cardinalities
        ranks = self.ranks

        # x & y are already in the same set
        if x_root == y_root:
            return

        self.count -= 1

        # x & y are not in the same set, we merge them
        x_rank = ranks[x]
        y_rank = ranks[y]

        if x_rank < y_rank:
            cardinalities[y_root] += cardinalities[x_root]
            parents[x_root] = y_root
        elif x_rank > y_rank:
            cardinalities[x_root] += cardinalities[y_root]
            parents[y_root] = x_root
        else:
            cardinalities[x_root] += cardinalities[y_root]
            parents[y_root] = x_root
            ranks[x_root] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def cardinality(self, x):
        parent = self.find(x)
        return self.cardinalities[parent]

    def components(self, min_size=1, max_size=float('inf')):
        n = self.capacity

        # Using counting sort
        # NOTE: can reduce memory footprint in dense cases, by computing k
        counts = [0] * n
        sorted_indices = [0] * n

        for i in range(n):
            counts[self.find(i)] += 1

        total = 0

        for i in range(n):
            current_count = counts[i]
            counts[i] = total
            total += current_count

        for i in range(n):
            parent = self.find(i)
            sorted_indices[counts[parent]] = i
            counts[parent] += 1

        # Iterating over components
        i = 0
        for _ in range(self.count):
            j = self.cardinalities[self.find(sorted_indices[i])]

            if j < min_size or j > max_size:
                i += j
                continue

            # NOTE: possibility to return islice
            component = sorted_indices[i:i + j]
            i += j
            yield component

    def __iter__(self):
        return self.components()

    def __getitem__(self, x):
        return self.find(x)

    def __repr__(self):
        return '<%s capacity=%i count=%i>' % (
            self.__class__.__name__,
            self.capacity,
            self.count
        )
