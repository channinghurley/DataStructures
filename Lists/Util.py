

def fold(l, acc, op):
    """Inspired by Scala's List.fold function, fold will recursively "fold" a list by applying operation "op" to the accumulator "acc" and each element of the list. Operation "op" should be a callable that will return the new accumulator. The result of op will become the new accumulator value for the next recursive step.
    """

    assert callable(op), "Operation must be callable."

    if l:
        return fold(l[1:], op(acc, l[0]), op)
    else:
        return acc
