import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def test_fibonacci_should_return_0_for_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_should_return_1_for_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_should_return_89_for_100(self):
        self.assertEqual(fibonacci(100), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
