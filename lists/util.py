
def ascending(l):
    """Return true if a list is sorted in strictly ascending order."""
    return all([l[i] <= l[i+1] for i in range(len(l) - 1)])

def descending(l):
    """Return True if a list is sorted in strictly descending order."""
    return ascending(list(reversed(l)))

def fold(l, acc, op):
    """Inspired by Scala's List.fold function, fold will recursively "fold" a list by applying operation "op" to the accumulator "acc" and each element of the list. Operation "op" should be a callable that will return the new accumulator. The result of op will become the new accumulator value for the next recursive step. Similar to functools.reduce, however the caller can maipulate the accumulator.
    """

    assert callable(op), "Operation must be callable."

    if l:
        return fold(l[1:], op(acc, l[0]), op)
    else:
        return acc
