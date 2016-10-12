#!/usr/bin/env python3

import sys
import time
# pode adicionar mais, porem para esse case-study apenas biblioteca padrão
# favor nao injetar time.sleep() no codigo dos outros
# depois podemos fazer em NumPy e outros para comparar

"""
Criteria:
* fastest runtime processing
* handles big data

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
                print("{:<20} {}".format(function.__name__, elapsed))
        
        
"""Algorithms"""

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



if len(sys.argv) != 2:
        print("Usage: sample_size\nExample: 50000000")
        sys.exit()

# generate list of integers (all odds, but one)
sample_size = int(sys.argv[1])
EVEN = 2
random_odds = [i for i in range(sample_size) if i % 2]
# insert one even number in the middle of the list
random_odds[int(sample_size / 2 / 2)] = EVEN  # outsider!


"""Run algorithms"""

benchmark(luiz_1, random_odds, EVEN)
benchmark(andrei_1, random_odds, EVEN)
