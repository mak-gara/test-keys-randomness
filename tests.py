import unittest

from random_sequence import generate_random_sequence
from key_randomness import KeyRandomness


class TestKeyRandomness(unittest.TestCase):

    def setUp(self):
        self.random_sequences = (generate_random_sequence("01", 20000) for _ in range(5))

    def key_randomness(self, test_function_name):
        for sequence in self.random_sequences:
            with self.subTest(sequence=sequence):
                key_randomness = KeyRandomness(sequence)
                test_function = getattr(key_randomness, test_function_name)
                self.assertTrue(test_function())

    def test_monobit(self):
        self.key_randomness("monobit")

    def test_check_max_series_length(self):
        self.key_randomness("check_max_series_length")

    def test_check_poker_test(self):
        self.key_randomness("check_poker_test")

    def test_check_series_length(self):
        self.key_randomness("check_series_length")


if __name__ == '__main__':
    unittest.main()
