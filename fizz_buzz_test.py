import unittest
from fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_should_return_empty_list_for_1(self):
        self.assertListEqual(fizz_buzz(1), [])

    def test_fizz_buzz_should_return_1_for_2(self):
        self.assertListEqual(fizz_buzz(2), ['1'])

    def test_fizz_buzz_should_contain_fizz_for_4(self):
        self.assertIn("Fizz", fizz_buzz(4))

