# =============================================================================
# Phylactery TrieDict Unit Tests
# =============================================================================
import pytest
from phylactery import TrieDict


class TestBitSet(object):
    def test_basics(self):
        trie = TrieDict()

        trie.set(['a', 'b', 'c'], 123)

        assert trie.get(['a', 'b', 'c']) == 123
        assert trie.get(['a', 'b']) is None
        assert trie.get([]) is None
        assert trie.get(['b', 'd']) is None
        assert trie.get(['a', 'b', 'c', 'd']) is None
        assert trie.get(['a', 'b'], 456) == 456

        trie[['a', 'b', 'c']] = 456

        assert trie.get(['a', 'b', 'c']) == 456

        assert trie[['a', 'b', 'c']] == 456

        with pytest.raises(KeyError):
            value = trie[['a', 'b']]

    def test_longest(self):
        trie = TrieDict()

        trie['roman'] = 1
        trie['romanesque'] = 2
        trie['john'] = 3
        trie['j'] = 2

        assert len(trie) == 4

        assert trie.longest('jo') == 2
        assert trie.longest('a') is None
        assert trie.longest('abcde') is None
        assert trie.longest('johnsie') == 3
        assert trie.longest('romani') == 1
        assert trie.longest('romanesque') == 2
        assert trie.longest('romanesques') == 2

    def test_iteration(self):
        trie = TrieDict()

        trie['abc'] = 1
        trie['def'] = 2

        assert set(trie.items()) == {('abc', 1), ('def', 2)}
        assert set(trie) == {('abc', 1), ('def', 2)}

        assert set(trie.keys()) == {'abc', 'def'}
        assert set(trie.values()) == {1, 2}
