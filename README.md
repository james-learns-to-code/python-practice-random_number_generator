# Mission 
Get random number by receiving decimal number 'n'

# Conditions
Random number should generated in range of 0...(n - 1)
Only use 'get_zero_or_one' function that returns 0 or 1


# Idea

There is a easy way to solve this problem by iterate range 0...n and add random generated bit for every loop. 
But it is too easy so i will find another way.

From the clue 0 or 1, i can easily infer that the key is bit-calculation.
If i convert decimal number 'n' to binary number 'b', i can make random number by mixing every digit in 'b'.
But mixed number 'r' could bigger than b because of b can have 0 bit.
So i will using circulation of number that does not exceeded 'n'.

For implementing this algorithm, i will calculate how many digit('d') that 'b' have.
Then generate binary number by shifting 'd' times.
While every shifting, will put the random binary number using 'get_zero_or_one'
In case of random number exceeded n, I will calculate difference of max number of shifting 'd' times and given number 'n'.
Then circulate random number by difference.


# Performance Comparison
```
leedongseok-ui-MacBook-Air:Riiid test leedongseok$ kernprof -l -v test.py
Wrote profile results to test.py.lprof
Timer unit: 1e-06 s

Total time: 0.024209 s
File: test.py
Function: test_get_random_by_another_way_by at line 129

Line       Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   129                                           @profile
   130                                           def test_get_random_by_another_way_by(given_number):
   131                                                print('test_get_random_by_another_way_by given_number: ', given_number)
   132         6          7.0      1.2      0.0      random_number_generator = lambda x: generate_random_number_by_bit_calculation(x)
   133         6      24202.0   4033.7    100.0      test_get_random_by(given_number, random_number_generator)

Total time: 11.8447 s
File: test.py
Function: test_get_random_by_easy_way_by at line 143

Line       Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   143                                           @profile
   144                                           def test_get_random_by_easy_way_by(given_number):
   145                                                print('test_get_random_by_easy_way_by given_number: ', given_number)
   146         6         12.0      2.0      0.0      random_number_generator = lambda x: generate_random_number_by_iterate_range(x)
   147         6   11844726.0 1974121.0    100.0      test_get_random_by(given_number, random_number_generator)

leedongseok-ui-MacBook-Air:Riiid test leedongseok$ 
```
