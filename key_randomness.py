import numpy as np
from numpy import ndarray
from math import ceil
from re import match


class KeyRandomness:
    """Class for assessing the randomness of a binary key sequence."""

    SEQUENCE_LENGTH = 20000
    LIMB_LENGTH = 32
    LOWER_FREQUENCY_BOUND = 9654
    UPPER_FREQUENCY_BOUND = 10346

    def __init__(self, sequence: str) -> None:
        """
        Initializes a KeyRandomness instance with a binary sequence for analysis.

        :param sequence: Sequence to be analyzed for randomness.
        :return: None
        """

        # check that the sequence length is equal to the SEQUENCE_LENGTH constant
        if len(sequence) != self.SEQUENCE_LENGTH:
            raise ValueError(
                f"Expected a string of length {self.SEQUENCE_LENGTH}, but got a string of length {len(sequence)}")

        # check that the sequence contains only a binary code
        if not match("^[01]+$", sequence):
            raise ValueError("Expected a string containing a binary code")

        self.limbs = self._split_bin_string(sequence, self.LIMB_LENGTH)

    @staticmethod
    def _split_bin_string(bin_string: str, segment_length: int) -> ndarray:
        """
        Splits a string containing a binary code into an array of numbers.
        The numbers are formed by converting the segments formed after splitting the string.
        The segment length limit is 32 bits.
        If the length of bin_string is not a multiple of segment_length,
        then the length of the last segment will differ from the specified segment_length.

        :param bin_string: String of binary code.
        :param segment_length: Length of the segments into which the string will be split.
        :return: NumPy array containing numbers formed by converting segments.
        """

        arr_length = ceil(len(bin_string) / segment_length)
        arr = np.zeros(arr_length, dtype=np.uint32)

        for i in range(arr_length):
            arr[i] = int(bin_string[i * segment_length: (i + 1) * segment_length], 2)

        return arr

    @staticmethod
    def _pad_with_zeros(bin_string: str, length: int) -> str:
        """
        Pads a binary string with zeros to match the specified length.

        :param bin_string: Binary string to pad.
        :param length: Desired length of the padded string.
        :return: Padded binary string.
        """

        padding = length - len(bin_string)
        if padding > 0:
            return "0" * padding + bin_string
        return bin_string

    def monobit(self) -> bool:
        """
        Performs the Monobit Frequency Test to assess the randomness of the binary sequence.

        :return: If the frequency of zeros in the binary code is in the range
        from LOWER_FREQUENCY_BOUND to UPPER_FREQUENCY_BOUND, not inclusive, then True, otherwise - False.
        """

        count = 0

        for limb in self.limbs:
            padded_limb = self._pad_with_zeros(bin(limb)[2:], self.LIMB_LENGTH)
            for bit in padded_limb:
                if bit == "0":
                    count += 1

        if self.LOWER_FREQUENCY_BOUND < count < self.UPPER_FREQUENCY_BOUND:
            return True
        return False
