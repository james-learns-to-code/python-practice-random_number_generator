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
