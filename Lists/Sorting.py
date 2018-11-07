"""Author: Channing J. Hurley
    Module: Sorting -- Implement the standard sorting algorithms
    Methods:
        *

    TODO:
        * quicksort
        * mergesort
        * bubble sort
        * selection sort
        * insertion sort
"""

import util

def insertion_sort(l):

    sorted_list, lp = [], l.copy()

    def get_pos(elem):
        for i, e in enumerate(lp):
            pass

    while lp:
        to_insert = lp.pop()
        sorted_list.insert(get_pos(to_insert), to_insert)
        # assert util.ascending(sorted_list), "Recursion invariant violated: list to append to is not sorted."
    return sorted_list

def mergesort(l):
    print("mergesort")

def quicksort(l):
    pass
