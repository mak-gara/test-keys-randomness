import unittest

from random_sequence import generate_random_sequence
from key_randomness import KeyRandomness


class TestKeyRandomness(unittest.TestCase):

    def setUp(self):
        self.random_sequences = (generate_random_sequence("01", 20000) for _ in range(5))

    def test_monobit(self):
        for sequence in self.random_sequences:
            with self.subTest(sequence=sequence):
                key_randomness = KeyRandomness(sequence)
                self.assertTrue(key_randomness.monobit())

    def test_check_max_series_length(self):
        for sequence in self.random_sequences:
            with self.subTest(sequence=sequence):
                key_randomness = KeyRandomness(sequence)
                self.assertTrue(key_randomness.check_max_series_length())


if __name__ == '__main__':
    unittest.main()
