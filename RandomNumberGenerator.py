
# Mission: Get random number by receiving decimal number 'n'
# Conditions: Random number should generated in range of 0...(n - 1)
#             Only use 'get_zero_or_one' function that returns 0 or 1


## MARK: Idea

# There is a easy way to solve this problem by  
# iterate range 0...n and add random generated bit for every loop. 
# But it is too easy so i will find another way.

# From the clue 0 or 1, i can easily infer 
# that the key is bit-calculation.
# If i convert decimal number 'n' to binary number 'b', 
# i can make random number by mixing every digit in 'b'.
# But mixed number 'r' could bigger than b because of b can have 0 bit.
# So i will using circulation of number that does not exceeded 'n'.

# For implementing this algorithm, 
# i will calculate how many digit('d') that 'b' have.
# Then generate binary number by shifting 'd' times.
# While every shifting,
# will put the random binary number using 'get_zero_or_one'
# In case of random number exceeded n, 
# I will calculate difference of
# max number of shifting 'd' times and given number 'n'.
# Then circulate random number by difference.


## MARK: Coding

from random import randrange
get_zero_or_one = lambda: randrange(2)

def get_random(max_number):

    # Easy way
    random_number = generate_random_number_by_iterate_range(max_number - 1)

    # Another way
    random_number = generate_random_number_by_bit_calculation(max_number - 1)
    return random_number

# Easy way - Implementation
def generate_random_number_by_iterate_range(number):
    random_number = 0
    for _ in range(number):
        random_bit = get_zero_or_one()
        random_number = random_number + random_bit
    return random_number
    
# Another way - Implementation

def generate_random_number_by_bit_calculation(number):
    bit_length = get_bit_length_of(number)
    random_number = generate_random_number_by(bit_length)
    max_number = generate_max_number_by(bit_length)
    random_number = circulate_number_with(max_number, random_number, number)
    return random_number

def circulate_number_with(max_number, random_number, number):
    difference = max_number - number
    random_number = random_number - difference
    return -random_number if random_number < 0 else random_number

def generate_random_number_by(bit_length):
    random_number = 0
    for _ in range(bit_length):
        random_number = random_number << 1
        random_bit = get_zero_or_one()
        random_number = random_number | random_bit
    return random_number

def generate_max_number_by(bit_length):
    max_number = 0
    for _ in range(bit_length):
        max_number = max_number << 1
        max_number = max_number | 1
    return max_number

def get_bit_length_of(number):
    bit_length = 0
    shift_counter = 1
    while number > 0:
        if (number & 1) == 1:
            bit_length = shift_counter
        number = number >> 1
        shift_counter = shift_counter + 1
    return bit_length

# MARK: Test

number_of_iterate = 100
list_of_given_number_for_testing = [5, 2, 6, 600, 314, 31344]

def test_generate_random_number_by_bit_length():
    test_generate_random_number_by(3, 7)
    test_generate_random_number_by(4, 15)

def test_generate_random_number_by(bit_length, expected_max_number):
    print('test_generate_random_number_by bit_length: ', bit_length)
    for _ in range(number_of_iterate):
        random_number = generate_random_number_by(bit_length)
        print('random_number: ', random_number)
        assert random_number <= expected_max_number, "Error: Exceeded random_number"

def test_get_bit_length_of_number():
    test_get_bit_length_of(3, 2)
    test_get_bit_length_of(5, 3)
    test_get_bit_length_of(100, 7)

def test_get_bit_length_of(number, expected_length):
    print('test_get_bit_length_of number: ', number)
    bit_length = get_bit_length_of(number)
    print('bit_length: ', bit_length)
    assert bit_length == expected_length, "Error: Inconsistency bit_length"

def test_get_random_number_by_another_way():
    for number in list_of_given_number_for_testing:
        test_get_random_number_by_another_way_in(number)

def test_get_random_number_by_another_way_in(given_number):
    print('test_get_random_number_by_another_way_in given_number: ', given_number)
    random_number_generator = lambda x: generate_random_number_by_bit_calculation(x)
    test_get_random_number_in(given_number, random_number_generator)

def test_get_random_number_by_easy_way():
    for number in list_of_given_number_for_testing:
        test_get_random_number_by_easy_way_in(number)

def test_get_random_number_by_easy_way_in(given_number):
    print('test_get_random_number_by_easy_way_in given_number: ', given_number)
    random_number_generator = lambda x: generate_random_number_by_iterate_range(x)
    test_get_random_number_in(given_number, random_number_generator)

def test_get_random_number_in(given_number, random_number_generator):
    assert given_number > 0, "Error: Minus or Zero are not supported"
    for _ in range(number_of_iterate):
        random_number = random_number_generator(given_number - 1)
        print('random_number: ', random_number)
        assert random_number < given_number, "Error: Exceeded random_number"


test_get_bit_length_of_number()
test_generate_random_number_by_bit_length()

# MARK: Main
test_get_random_number_by_easy_way()
test_get_random_number_by_another_way()


## MARK: Performance Comparison

# leedongseok-ui-MacBook-Air:Riiid test leedongseok$ kernprof -l -v test.py
# Wrote profile results to test.py.lprof
# Timer unit: 1e-06 s

# Total time: 0.024209 s
# File: test.py
# Function: test_get_random_by_another_way_by at line 129

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#    129                                           @profile
#    130                                           def test_get_random_by_another_way_by(given_number):
#    131                                               # print('test_get_random_by_another_way_by given_number: ', given_number)
#    132         6          7.0      1.2      0.0      random_number_generator = lambda x: generate_random_number_by_bit_calculation(x)
#    133         6      24202.0   4033.7    100.0      test_get_random_by(given_number, random_number_generator)

# Total time: 11.8447 s
# File: test.py
# Function: test_get_random_by_easy_way_by at line 143

# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#    143                                           @profile
#    144                                           def test_get_random_by_easy_way_by(given_number):
#    145                                               # print('test_get_random_by_easy_way_by given_number: ', given_number)
#    146         6         12.0      2.0      0.0      random_number_generator = lambda x: generate_random_number_by_iterate_range(x)
#    147         6   11844726.0 1974121.0    100.0      test_get_random_by(given_number, random_number_generator)

# leedongseok-ui-MacBook-Air:Riiid test leedongseok$ 
