# =============================================================================
# Phylactery TrieDict
# =============================================================================
#
# A simple Python implementation of a (key, value) Trie.
#


class TrieDictNode(object):
    __slots__ = ('children', 'value')

    def __init__(self):
        self.children = None
        self.value = None


class TrieDict(object):
    __slots__ = ('__root', '__shape', '__size')

    def __init__(self, shape=str):
        self.__root = TrieDictNode()
        self.__shape = shape
        self.__size = 0

    def __len__(self):
        return self.__size

    def set(self, key, value):
        node = self.__root

        for char in key:

            if node.children is None:
                child = TrieDictNode()

                node.children = {
                    char: child
                }

                node = child
                continue

            child = node.children.get(char)

            if child is not None:
                node = child
            else:
                child = TrieDictNode()

                node.children[char] = child
                node = child

        if node.value is None:
            self.__size += 1

        node.value = value

    def __setitem__(self, key, value):
        return self.set(key, value)

    def get(self, key, default=None):
        node = self.__root

        for char in key:
            if node.children is None:
                return default

            child = node.children.get(char)

            if child is None:
                return default

            node = child

        if node.value is not None:
            return node.value

        return default

    def __getitem__(self, key):
        node = self.__root

        for char in key:
            if node.children is None:
                raise KeyError(key)

            child = node.children.get(char)

            if child is None:
                raise KeyError(key)

            node = child

        if node.value is not None:
            return node.value

        raise KeyError(key)

    def longest(self, key):
        node = self.__root

        last_value = None

        for char in key:

            if node.value is not None:
                last_value = node.value

            if node.children is None:
                break

            child = node.children.get(char)

            if child is None:
                break

            node = child

        if node.value is not None:
            return node.value

        return last_value

    def items(self):
        stack = [(self.__root, self.__shape())]

        while len(stack) > 0:
            node, key = stack.pop()

            if node.value:
                yield (key, node.value)

            if node.children is None:
                continue

            for char, child in node.children.items():
                stack.append((child, key + char))

    def keys(self):
        stack = [(self.__root, self.__shape())]

        while len(stack) > 0:
            node, key = stack.pop()

            if node.value:
                yield key

            if node.children is None:
                continue

            for char, child in node.children.items():
                stack.append((child, key + char))

    def values(self):
        stack = [self.__root]

        while len(stack) > 0:
            node = stack.pop()

            if node.value:
                yield node.value

            if node.children is None:
                continue

            stack.extend(node.children.values())

    def __iter__(self):
        return self.items()
