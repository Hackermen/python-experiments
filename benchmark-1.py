#!/usr/bin/env python3

import sys
import time
# you may import others, but for this case-study use only standard library
# please do not add time.sleep() into someone else's algorithm :^)
# later compare with NumPy to see how optmized they actually are?

"""
Criteria:
* fastest runtime processing
* handles big data without crashing

You are given an array (which will have a length of at least 3,
but could be very large) containing int_list.
The array is either entirely comprised of odd int_list or
entirely comprised of even int_list except for a single integer N.
Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160
"""

def benchmark(function, big_list, expected_output):
        start = time.time()
        if function(big_list) == expected_output:
                elapsed = time.time() - start
                print("{:<20} {:.2f}".format(function.__name__, elapsed))


"""
Algorithms
"""

def luiz_1(int_list):
    if int_list[0] % 2 == int_list[1] % 2:
        return next((x for x in int_list[2:] if x % 2 != int_list[0] % 2), None)
    elif int_list[0] % 2 == int_list[2] % 2:
        return int_list[1]
    else:
        return int_list[0]


def andrei_1(int_list):
    odds = [x for x in int_list if x % 2]
    evens = set(odds) ^ set(int_list)
    if len(evens) > len(odds): return odds.pop()
    return evens.pop()

"""
Main
"""

# int_list size
sample_size = 30000000  # 30 millions
#sample_size = 500000000  # for BIG DATA testing, 500 millions. Some algorithms may (will) crash your computer

try:
    sample_size = int(sys.argv[1])  # or pass one by command-line argument
except IndexError:
    pass

# generate list of integers (all odds, but one)
EVEN = 2
random_odds = [i for i in range(sample_size) if i % 2]
# insert one even number in the middle of the list
random_odds[int(sample_size / 2 / 2)] = EVEN  # outsider

"""
Run algorithms
"""

benchmark(luiz_1, random_odds, EVEN)
benchmark(andrei_1, random_odds, EVEN)
