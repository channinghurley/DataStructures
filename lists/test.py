"""Author: Channing J. Hurley

    Module: lists.test.py -- Unit test driver file for lists package.

    TODO:

"""

import sorting
import random

def get_inputs():
    """"""
    inp1 = []
    inp2 = [1]
    inp3 = list(reversed(range(10)))
    inp4 = [random.randint(-50, 50) for i in range(100)]
    return (inp1, inp2, inp3, inp4)

def test(f, l):
    """Test function f with input list l. Return True if correct result is achieved, False otherwise"""
    res = f(l)
    print(res)
    return res == sorted(l)

if __name__ == "__main__":

    attrs = [getattr(sorting, attr) for attr in dir(sorting)]
    functions = list(filter(callable, attrs))

    for function in functions:
        if function.__name__ == "insertion_sort":
            for input in get_inputs():
                result = test(function, input)
                print(result)
