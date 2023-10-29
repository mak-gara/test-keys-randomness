# Testing keys for randomness according to the FIPS-140 standard

This project implements the following tests to check the randomness of sequences:

- **Monobit test**: checks whether the balance between zeros and ones in the sequence is maintained.
- **Maximum series length test**: checks whether the sequence contains a series of identical bits of too long a length.
- **Poker test**: checks whether the bits are evenly distributed in the blocks of the sequence.
- **Series length test**: checks whether the sequence contains too long or too short series of identical bits.

These tests allow you to assess the statistical randomness of bit sequences. If the sequence fails the randomness tests, it may indicate the presence of some patterns or deviations from a random distribution, which can threaten the security of cryptographic systems.

## Usage

### Generation of random sequences for testing
Before testing a sequence, you need to generate it. This can be done using the `generate_random_sequence()` function from the `random_sequence` module. It takes two parameters as arguments:
- `character_source`: a string containing the characters to generate the sequence.
- `length`: the length of the generated sequence is represented by a number.

The code below will generate a binary sequence of length 20000.
```python
from random_sequence import generate_random_sequence

sequence = generate_random_sequence("01", 20000)
```

### Generation of random sequences for testing
To check a pre-generated sequence, you need to create an object of the `KeyRandomness` class from the `key_randomness` module. When initializing the object, you need to pass the generated sequence for testing.

Then we simply call the necessary testing methods of the newly created object. This is shown in the code below.

```python
from key_randomness import KeyRandomness

key_randomness = KeyRandomness(sequence)

print(f"Did the sequence pass the monobit test? - {key_randomness.monobit()}")
print(f"And the maximum series length test? - {key_randomness.check_max_series_length()}")
print(f"What about the Poker test? - {key_randomness.check_poker_test()}")
print(f"And finally, the series length test? - {key_randomness.check_series_length()}")
```

### Running Tests
To run the tests for this code, execute the tests.py file.

```shell
python tests.py
```
This will run a series of tests to verify the correctness of the methods of the `KeyRandomness` class for testing sequences for randomness.