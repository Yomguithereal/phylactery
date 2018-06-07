# =============================================================================
# Phylactery Vantage Point Tree
# =============================================================================
#
# Python implementation of a Vantage Point Tree (VPTree) that can index items
# in metric space and perform efficient k-nn queries.
#
import numpy as np


class VPTreeNode(object):
    """
    Class representing a VPTree's node.

    """

    __slots__ = ('left', 'mu', 'right', 'value')

    def __init__(self, value):
        self.value = value
        self.mu = 0.0
        self.left = None
        self.right = None

    def __repr__(self):
        return '<%s value=%s mu=%i>' % (
            self.__class__.__name__,
            self.value,
            self.mu
        )


class VPTree(object):
    """
    The VPTree class.

    Args:
        capacity (number): total number of items to store.

    """

    __slots__ = ('count', 'distance', 'root')

    def __init__(self, items, distance):

        if type(items) is not list:
            items = list(items)

        # Properties
        self.distance = distance
        self.root = VPTreeNode(items[0])
        self.count = len(items)

        # Building the tree
        stack = [(self.root, list(range(1, self.count)))]

        while len(stack) != 0:
            vp, values = stack.pop()

            # We compute distances from vp to other points
            distances = [0] * len(values)
            for i, v in enumerate(values):
                distances[i] = distance(vp.value, items[v])

            # And we split at median
            mu = np.median(distances)
            vp.mu = mu

            left = []
            right = []

            for i, v in enumerate(values):
                if distances[i] < mu:
                    left.append(v)
                else:
                    right.append(v)

            if len(right):
                node = VPTreeNode(items[right.pop()])
                vp.right = node

                if len(right):
                    stack.append((node, right))

            if len(left):
                node = VPTreeNode(items[left.pop()])
                vp.left = node

                if len(left):
                    stack.append((node, left))

    def __len__(self):
        return self.count

    def dfs(self):
        stack = [(0, self.root)]

        while len(stack) != 0:
            level, node = stack.pop()

            yield level, node

            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))

    def neighbors_in_radius(self, query, radius):
        stack = [self.root]
        distance = self.distance

        while len(stack) != 0:
            node = stack.pop()

            d = distance(node.value, query)

            if d <= radius:
                yield (node.value, d)

            mu = node.mu

            if d < mu:
                if node.left and d < mu + radius:
                    stack.append(node.left)
                if node.right and d >= mu - radius:
                    stack.append(node.right)
            else:
                if node.right and d >= mu - radius:
                    stack.append(node.right)
                if node.left and d < mu + radius:
                    stack.append(node.left)
