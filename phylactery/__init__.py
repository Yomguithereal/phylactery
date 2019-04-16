import sys

PY2 = sys.version.startswith('2')

# Not python2 compatible
if not PY2:
    from phylactery.unionfind import UnionFind
    from phylactery.vptree import VPTree

# python2 compatible
from phylactery.bitset import BitSet
from phylactery.triedict import TrieDict
