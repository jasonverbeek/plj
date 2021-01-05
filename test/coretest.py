from unittest import TestCase
from copy import deepcopy
from functools import reduce

from plj.core import get_in, filter, conj, into, first, last, nth

class CoreTest(TestCase):

    def test_get_in(self):
        data = {
            "a": 2,
            "b": {
                "ba": 1,
                "bb": {
                    "type": "company",
                }
            },
            "c": {
                "ca": {
                    "type": False,
                },
                "cb": {
                    "cba": None,
                    "cbb": 0,
                }
            }
        }

        original = deepcopy(data)

        self.assertEqual(2, get_in(data, "a"))
        self.assertEqual(1, get_in(data, "b", "ba"))
        self.assertEqual("company", get_in(data, "b", "bb", "type"))

        self.assertEqual(False, get_in(data, "c", "ca", "type"))
        self.assertEqual(None, get_in(data, "c", "cb", "cba"))
        self.assertEqual(0, get_in(data, "c", "cb", "cbb"))

        self.assertEqual(None, get_in(data, "d", "da", "daa"))
        self.assertEqual(42, get_in(data, "d", "da", "daa", default=42))

        self.assertEqual(42, get_in(data, "c", "cb", "cba", default=42))

        self.assertEqual(original, data)


    def test_filter(self):
        data = [1, 2, 3, 0, False, None, "q", "a", "z"]

        boolfilter = filter(bool)
        self.assertTrue(callable(boolfilter))
        self.assertEqual([1, 2, 3, 'q', 'a', 'z'], list(boolfilter(data)))

        strfilter = filter(lambda x: isinstance(x, str))
        self.assertTrue(callable(strfilter))
        self.assertEqual(['q', 'a', 'z'], list(strfilter(data)))

        self.assertEqual([2], list(filter(lambda x: x==2, data)))

    def test_into(self):
        lst = []
        self.assertEqual([1, 2], list(into(lst, [1, 2])))
        self.assertEqual([], lst)
        self.assertEqual([2, 1, 1, 2], list(into([2, 1], [1, 2])))

    def test_conj(self):
        lst = []

        self.assertEqual([1], list(conj(lst, 1)))
        self.assertEqual([], lst)

        self.assertEqual([1, 2, 3, 4], list(reduce(conj, [3, 4], [1, 2])))

    def test_first(self):
        self.assertEqual(1, first([1, "B", 3, "D", 5]))
        self.assertEqual(0, first((x for x in range(5))))
        self.assertEqual(None, first((x for x in range(0))))

    def test_last(self):
        self.assertEqual(5, last([1, "B", 3, "D", 5]))
        self.assertEqual(4, last((x for x in range(5))))
        self.assertEqual(None, last((x for x in range(0))))

    def test_nth(self):
        self.assertEqual("B", nth([1, "B", 3, "D", 5], 1))
        self.assertEqual(None, nth([1, "B", 3, "D", 5], 7))
        self.assertEqual(3, nth((x for x in range(5)), 3))
        self.assertEqual(None, nth((x for x in range(0)), 2))

