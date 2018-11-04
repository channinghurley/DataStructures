"""Author: Channing J. Hurley

    Module: lists.test.py -- Unit test driver file for lists package.

    TODO:

"""

import sorting

def get_inputs():
    """"""
    inp1 = []
    inp2 = [1]
    inp3 = list(reversed(range(10)))
    inp4 = [random.randint(-50, 50) for i in range(100)]

def test(f, l):
    """Test function f with input list l. Return True if correct result is achieved, False otherwise"""

    res = f(l)
    return res == sorted(l)

if __name__ == "__main__":

    attrs = [getattr(sorting, a) for a in dir(sorting)]
    functions = list(filter(callable, attrs))
