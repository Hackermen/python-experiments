#!/usr/bin/env python3

import sys
import time
# you can import others, for this case-study use only standard library

"""
CRITERIA:
* fastest runtime processing - wins
* can handle big data - bonus
* support both 'odd number lists' and 'even number lists'

PROBLEM:
You are given an array which will have a length of at least 3,
but could be very large. The array is either entirely comprised of odd integers
or entirely comprised of even integers except for a single integer N.
Write a function that takes the array as an argument and returns N.

For example:

[10, 5, 20]
Return: 5

[2, 4, 0, 100, 4, 11, 2602, 36]
Return: 11

[160, 3, 1719, 19, 11, 13, -21]
Return: 160
"""

def benchmark(function, int_list, expected_output):
        # simple unit testing
        tests = []
        tests.append(function([0, 1, 1, 1]) == 0)  # even: first
        tests.append(function([1, 0, 1, 1]) == 0)  # even: second/middle
        tests.append(function([1, 1, 1, 0]) == 0)  # even: last
        tests.append(function([1, 0, 0, 0]) == 1)  # odd:  first
        tests.append(function([0, 1, 0, 0]) == 1)  # odd:  second/middle
        tests.append(function([0, 0, 0, 1]) == 1)  # odd:  last
        if False in tests:
            print('{:<12} failed tests'.format(function.__name__))
            return

        start = time.time()
        if function(int_list) == expected_output:
                elapsed = time.time() - start
                print("{:<12} {:.3f}".format(function.__name__, elapsed))


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
    if len(evens) >= len(odds): return odds.pop()
    return evens.pop()


def rodrigo_1(int_list):
    odds = list(filter(lambda x: x % 2, int_list))
    evens = set(int_list) - set(odds)
    if len(evens) >= len(odds): return odds.pop()
    return evens.pop()


def luiz_2(int_list):
    parity = [n % 2 for n in int_list]
    return int_list[parity.index(1)] if sum(parity) == 1 else int_list[parity.index(0)]


def andrei_2(int_list):
    checks = []
    checks.append(int_list[0] % 2 == 0)
    checks.append(int_list[1] % 2 == 0)
    checks.append(int_list[2] % 2 == 0)
    if checks.count(True) >= 2:
        for i in int_list:
            if i % 2 != 0:
                return i
    else:
        for i in int_list:
            if i % 2 == 0:
                return i
"""
Main
"""

# int_list size
sample_size = 30000000  # 30 millions

try:
    sample_size = int(sys.argv[1])  # or pass one by command-line argument
except IndexError:
    pass

# generate list of integers (all odds, but one)
random_odds = [i for i in range(sample_size) if i % 2]
EVEN = 0
# insert one even number in the middle of the list
random_odds[int(sample_size / 2 / 2)] = EVEN  # outsider

"""
Run algorithms
"""

benchmark(luiz_1, random_odds, EVEN)
benchmark(andrei_1, random_odds, EVEN)
benchmark(rodrigo_1, random_odds, EVEN)
benchmark(luiz_2, random_odds, EVEN)
benchmark(andrei_2, random_odds, EVEN)
