from re import match


class KeyRandomness:
    """Class for assessing the randomness of a binary key sequence."""

    SEQUENCE_LENGTH = 20000
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

        self.input_sequence = sequence

    def monobit(self) -> bool:
        """
        Performs the Monobit Frequency Test to assess the randomness of the binary sequence.

        :return: If the frequency of zeros in the binary code is in the range
        from LOWER_FREQUENCY_BOUND to UPPER_FREQUENCY_BOUND, not inclusive, then True, otherwise - False.
        """

        count = 0

        for bit in self.input_sequence:
            if bit == "0":
                count += 1

        if self.LOWER_FREQUENCY_BOUND < count < self.UPPER_FREQUENCY_BOUND:
            return True
        return False
