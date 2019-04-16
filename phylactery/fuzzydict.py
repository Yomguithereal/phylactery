# =============================================================================
# Phylactery FuzzyDict
# =============================================================================
#
# Simple sugar over a dict that processes given key on read/write for
# fuzzy matching purposes.
#
from collections import defaultdict


class FuzzyDict(object):

    def __init__(self, getters):
        self.__data = {}

        if callable(getters):
            self.__write_getter = getters
            self.__read_getter = getters
        else:
            self.__write_getter = getters[0]
            self.__read_getter = getters[1]


class FuzzyDefaultDict(FuzzyDict):

    def __init__(self, getters, constructor):
        self.__data = defaultdict(constructor)

        if callable(getters):
            self.__write_getter = getters
            self.__read_getter = getters
        else:
            self.__write_getter = getters[0]
            self.__read_getter = getters[1]
