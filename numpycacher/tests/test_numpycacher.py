import unittest
import numpy as np
from ..numpycacher import quickcacher, unicacher


class TestNumpyQuickCacher(unittest.TestCase):

    def test_name_saved(self):
        cache_f = {}

        @quickcacher(cache_f, 1)
        def f(x, a, b):
            return a*x + b

        self.assertEqual(f.__name__, 'f')

    def test_equal_cached_value(self):
        cache_f = {}

        @quickcacher(cache_f, 1)
        def f(x, a, b):
            return a*x + b

        value = f(np.array([1, 2]), 1, 0)
        self.assertTrue((value == cache_f.popitem()[1]).all())

    def test_cache_size(self):
        cache_f = {}

        @quickcacher(cache_f, 1, 10)
        def f(x, a, b):
            return a*x + b

        for i in range(20):
            with self.subTest(i=i):
                f(np.array([1, 2]), 1, i)
                self.assertLessEqual(len(cache_f), 10)


class TestNumpyUniCacher(unittest.TestCase):

    def test_name_saved(self):
        cache_f = {}

        @unicacher(cache_f)
        def f(x, a, b):
            return a*x + b

        self.assertEqual(f.__name__, 'f')

    def test_equal_cached_value(self):
        cache_f = {}

        @unicacher(cache_f)
        def f(x, a, b):
            return a*x + b

        value = f(np.array([1, 2]), 1, 0)
        self.assertTrue((value == cache_f.popitem()[1]).all())

    def test_equal_different_enter_points(self):
        cache_f = {}

        @unicacher(cache_f)
        def f(x, a, b, y):
            return a*x + b*y

        value = f(np.array([1, 2]), 1, 1, np.array([1, 2]))
        self.assertTrue((value == cache_f.popitem()[1]).all())

    def test_cache_size(self):
        cache_f = {}

        @unicacher(cache_f, 10)
        def f(x, a, b):
            return a*x + b

        for i in range(20):
            with self.subTest(i=i):
                f(np.array([1, 2]), 1, i)
                self.assertLessEqual(len(cache_f), 10)
