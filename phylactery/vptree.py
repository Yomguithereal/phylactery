# =============================================================================
# Phylactery Vantage Point Tree
# =============================================================================
#
# Python implementation of a Vantage Point Tree (VPTree) that can index items
# in metric space and perform efficient k-nn queries.
#
import math
import random
from statistics import median, pvariance

# TODO: fails if only 1 item given


class VPTreeNode(object):
    """
    Class representing a Vantage Point Tree's node.

    Args:
        value (any): The node's value.

    Attributes:
        left (VPTreeNode): Left child.
        right (VPTreeNode): Right child.
        mu (int or float): Median threshold.
        value (any): The node's value.

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
    Class representing a Vantage Point Tree.

    Args:
        items (iterable): Items to index in the tree.
        distance (callable): Distance function to use.
        selection (str, optional): Vantage point selection mode to choose
            between "arbitrary", "random" and "spread". Defaults to "arbitrary".

    """

    __slots__ = ('count', 'distance', 'root', 'selection')

    def __init__(self, items, distance, selection='arbitrary'):

        if type(items) is not list:
            items = list(items)

        # Properties
        self.distance = distance
        self.selection = selection
        self.count = len(items)

        # Initializing root
        index, indices = self.__select(list(range(self.count)), items)
        self.root = VPTreeNode(items[index])

        # Building the tree
        stack = [(self.root, indices)]

        while len(stack) != 0:
            vp, values = stack.pop()

            # We compute distances from vp to other points
            distances = [0] * len(values)
            for i, v in enumerate(values):
                distances[i] = distance(vp.value, items[v])

            # And we split at median
            mu = median(distances)
            vp.mu = mu

            left = []
            right = []

            for i, v in enumerate(values):
                if distances[i] < mu:
                    left.append(v)
                else:
                    right.append(v)

            if len(right):
                index, right = self.__select(right, items)
                node = VPTreeNode(items[index])
                vp.right = node

                if len(right):
                    stack.append((node, right))

            if len(left):
                index, left = self.__select(left, items)
                node = VPTreeNode(items[index])
                vp.left = node

                if len(left):
                    stack.append((node, left))

    def __len__(self):
        return self.count

    def __select(self, indices, values):
        selection = self.selection

        if selection == 'arbitrary':
            index = indices.pop()
            return index, indices

        if selection == 'random':
            random.shuffle(indices)
            index = indices.pop()
            return index, indices

        if selection == 'spread':
            distance = self.distance

            s = min(math.ceil(len(indices) * 0.1), 100)

            P = random.sample(indices, s)
            best_spread = float('-inf')
            best_p = None

            for p in P:
                D = random.sample(indices, s)
                M = [0] * s

                for i in range(s):
                    M[i] = distance(values[p], values[D[i]])

                spread = pvariance(M)

                if spread > best_spread:
                    best_spread = spread
                    best_p = p

            indices.pop(indices.index(best_p))

            return best_p, indices

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

            if node.left and d < mu + radius:
                stack.append(node.left)

            if node.right and d >= mu - radius:
                stack.append(node.right)
