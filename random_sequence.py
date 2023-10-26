import random


def generate_random_sequence(character_source: str, length: int) -> str:
    """
    Generate a random sequence of characters from the given character source.

    :param character_source: The source of characters to choose from.
    :param length: The length of the random sequence to generate.
    :return: A random sequence of characters with the specified length.
    """

    random_sequence = ""

    for _ in range(length):
        index = random.randint(0, len(character_source) - 1)
        random_sequence += character_source[index]

    return random_sequence
