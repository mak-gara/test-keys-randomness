import unittest

from random_sequence import generate_random_sequence
from key_randomness import KeyRandomness


class TestKeyRandomness(unittest.TestCase):

    def test_monobit(self):
        random_sequences = (generate_random_sequence("01", 20000) for _ in range(5))

        for sequence in random_sequences:
            with self.subTest(sequence=sequence):
                key_randomness = KeyRandomness(sequence)
                self.assertTrue(key_randomness.monobit())


if __name__ == '__main__':
    unittest.main()
