import unittest

from prime_numbers import prime_numbers

class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers_should_return_False_for_1(self):
        self.assertFalse(prime_numbers(1), False)

    def test_prime_numbers_should_return_2_for_2(self):
        self.assertEqual(prime_numbers(2), [2])

    def test_prime_numbers_should_return_3_for_3(self):
        self.assertEqual(prime_numbers(3), [2,3])

    def test_prime_numbers_should_not_return_4_for_5(self):
        self.assertNotIn(prime_numbers(5), [2,3,5])

    def test_prime_numbers_should_contain_13_in_15(self):
        self.assertIn(prime_numbers(15), [[2, 3, 5, 7, 11, 13]])




