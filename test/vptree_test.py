# =============================================================================
# Phylactery VPTree Unit Tests
# =============================================================================
from Levenshtein import distance as levenshtein
from phylactery import VPTree

WORDS = [
    'book',
    'back',
    'bock',
    'lock',
    'mack',
    'shock',
    'ephemeral',
    'magistral',
    'shawarma',
    'falafel',
    'onze',
    'douze',
    'treize',
    'quatorze',
    'quinze'
]

RADIUS_2 = set([
    ('bock', 2),
    ('book', 1),
    ('lock', 1)
])

RADIUS_3 = set([
    ('bock', 2),
    ('book', 1),
    ('lock', 1),
    ('shock', 3),
    ('mack', 3),
    ('back', 3)
])


class TestVPTree(object):
    def test_basics(self):
        tree = VPTree(WORDS, levenshtein)

        assert len(tree) == len(WORDS)

        assert set(tree.neighbors_in_radius('look', 2)) == RADIUS_2
        assert set(tree.neighbors_in_radius('look', 3)) == RADIUS_3

    def test_random_selection(self):
        tree = VPTree(WORDS, levenshtein, selection='random')

        assert len(tree) == len(WORDS)

        assert set(tree.neighbors_in_radius('look', 2)) == RADIUS_2
        assert set(tree.neighbors_in_radius('look', 3)) == RADIUS_3

    def test_spread_selection(self):
        tree = VPTree(WORDS, levenshtein, selection='spread')

        assert len(tree) == len(WORDS)

        assert set(tree.neighbors_in_radius('look', 2)) == RADIUS_2
        assert set(tree.neighbors_in_radius('look', 3)) == RADIUS_3
