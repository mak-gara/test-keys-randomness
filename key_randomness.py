from re import match


class KeyRandomness:
    """Class for assessing the randomness of a binary key sequence."""

    SEQUENCE_LENGTH = 20000
    MONOBIT_LOWER_FREQUENCY = 9654
    MONOBIT_UPPER_FREQUENCY = 10346
    MAX_SERIES_LENGTH = 36
    POKER_M = 4
    POKER_LOWER_FREQUENCY = 1.03
    POKER_UPPER_FREQUENCY = 57.4

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
        from MONOBIT_LOWER_FREQUENCY to MONOBIT_UPPER_FREQUENCY, not inclusive, then True, otherwise - False.
        """

        count = 0

        for bit in self.input_sequence:
            if bit == "0":
                count += 1

        if self.MONOBIT_LOWER_FREQUENCY < count < self.MONOBIT_UPPER_FREQUENCY:
            return True
        return False

    def check_max_series_length(self) -> bool:
        """
        Checks if the binary sequence complies with the maximum series length constraint.

        :return: True if the binary sequence meets the maximum series length requirement, otherwise False.
        """

        previous_bit = self.input_sequence[0]
        counter = 1

        for i in range(1, len(self.input_sequence)):
            bit = self.input_sequence[i]

            if bit == previous_bit:
                counter += 1
                if counter >= self.MAX_SERIES_LENGTH:
                    return False
            else:
                counter = 1

            previous_bit = bit

        return True

    def check_poker_test(self) -> bool:
        """
        Checks if the input sequence passes a Poker Test for randomness.

        The Poker Test is used to assess the randomness of a binary sequence. It divides the sequence
        into segments and calculates a statistic, X3, to determine whether the sequence exhibits patterns
        or biases. If X3 falls within the specified range (POKER_LOWER_FREQUENCY, POKER_UPPER_FREQUENCY),
        the sequence is considered random, and the method returns True. Otherwise, it returns False.

        :return: True if the sequence is considered random by the Poker Test, False otherwise.
        """

        k = self.SEQUENCE_LENGTH // self.POKER_M
        frequency_counter = {}

        # count the number of times certain blocks occur
        for i in range(k):
            segment = self.input_sequence[i * self.POKER_M: (i + 1) * self.POKER_M]
            if segment in frequency_counter:
                frequency_counter[segment] += 1
            else:
                frequency_counter[segment] = 1

        # summation
        sum = 0
        frequence_list = list(frequency_counter.values())
        for i in range(0, 2 ** self.POKER_M):
            try:
                sum += frequence_list[i] ** 2
            # IndexError raises when the number of unique Poker blocks is less than 16
            # in this case, the formula for calculating X3 does not work
            except IndexError:
                return False

        x3 = 2 ** self.POKER_M / k * sum - k

        if self.POKER_LOWER_FREQUENCY < x3 < self.POKER_UPPER_FREQUENCY:
            return True
        return False
