"""File for tinkering"""

from itertools import islice
from time import time

# from Trees.BinaryTree import Node
# from Trees.Util import *
# from Lists.Util import fold as list_fold
from trees.binary_tree import Node
from trees.util import *
from trees.bst import Bst

tree = Bst("F", Bst("B", Bst("A"), Bst("D", Bst("C"), Bst("E"))), Bst("G", Bst("I", left=Bst("H"))))
bfs(tree, lambda n: print(n.data, end=' '))
print(issorted(tree)) 


# l = [i for i in range(-10, 10)]
# print(len(l))
# t = Bst.from_list(l)
# bfs(t, lambda n: print(n.data, end=' '))
# print("\n", depth(find(Node(9), t), t))



# t2 = Bst.from_list([i for i in range(-3, 4)])
# print(t2)
# in_order_dfs(t2, lambda n: print(n.data, end=' '))
# print("\n", t2.data, "\n")
#
# t3 = Bst.from_list([i for i in reversed(range(-3, 4))])
# in_order_dfs(t2, lambda n: print(n.data, end=' '))
# # t3.set_right(Bst(1))
# print(t3)
# print(issorted(t3))

# l = [-i if i % 2 else i for i in range(10)]
# print(l)
# t = Bst.from_list(l)
# print(t)
# in_order_dfs(t, lambda n: print(n.data, end=' '))

# def timed(f):
#     """Decorator to time function calls."""
#     def caller(*args):
#         start = time()
#         res = f(*args)
#         return res, time() - start
#     return caller
#
# fib_act = [
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
#     55, 89, 144, 233, 377, 610, 987,
#     1597, 2584, 4181, 6765, 10946,
#     17711, 28657, 46368, 75025,
#     121393, 196418, 317811
# ]
#
# @timed
# def fib(n):
#     """Return the n-th number of the fibonacci sequence. Iterative; relatively memory-inefficient."""
#     seq = [0, 1]
#     while len(seq) < n:
#         seq.append(seq[-1] + seq[-2])
#     return seq[n-1]
#
# @timed
# def fib_rec(n):
#     """Return the n-th number of the fibonacci sequence. Recursive, far less efficient than
#     iterative and generative implementations."""
#     if n <= 1:
#         return n
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)
#
# def gen_fib():
#     """Return an infinite stream of the fibonacci sequence as a generator. More memory and time
#     efficient than the iterative implementation. Use islice or a list comprehension to get a finite
#     slice of the infinite sequence.
#     """
#
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# @timed
# def get_fib(n):
#     """Get the n-th fibonacci number using the gen_fib generator (n is 0 based)."""
#     return next(islice(gen_fib(), n, n + 1))
#
# # print(get_fib(20))
#
#
# # g = gen_fib()
#
#
#
#
# def test(n):
#     i = 0
#     while i < n:
#         sent = (yield i)
#         i = sent if sent else i + 1
# # from Trees.BinaryTree import Node
# # from Trees.Util import *
# # from Lists.Util import fold as list_fold
# # from trees.binary_tree import *
# # from trees.util import bfs
#
# t = Node(Node(data=2), 1, Node(data=3))
# n = Node(data=5)

# print(t)
#
# t1 = Node()
# t2 = Node()
# print(t1 == t2)




#n.set_left(tree)

#bfs(tree, lambda n: print(n.data))


# t2 = Node(Node(None, None, None), 1, Node(None, None, None))
# print(t2)

# l = [1,2,3,4,5]

# print(l*2)

# print(list(map(lambda x: print(x), l)))



#
# test = Node(data=1, left=Node(data=1))
# tree = Node(Node(Node(data="A"), "B", Node(Node(data="C"), "D", Node(data="E"))), "F", Node(None, "G", Node(Node(data="H"), "I")))
#
# tree2 = Node(Node(Node(data=4), 2, Node(data=5)), 1, Node(Node(data=6), 3, Node(data=7)))

# g = test(10)
# print(next(g))
# g.send(5)
# print(next(g))

# print(list(gen_fib())[28]) # Don't do this; highly inefficient
# print(get_fib(28))

# iter_res, itime = fib(101)
# gen_res, gtime = get_fib(100)
'''
assert iter_res == gen_res, "Solution do not match!"
print("Iterative:", itime)
print("Recursive:", fib_rec(28)[1])
print("Generative:", gtime)
print("Winner:", "Iterative" if itime < gtime else "Generative")
'''



# first_29 = [i for i in islice(gen_fib(), 20, 29)]
# print(first_29)
# print(fib_act[20])
# print(first_29 == fib_act)

# def fib_rec(n, seq=None):
#     """Return the n-th number of the fibonacci sequence."""
#     if seq:
#         if n <= len(seq):
#             return seq[n-1]
#
# correct = all([fib(i) == fib_rec(i, fib_act) for i in range(1, 30)])
# print(correct)

# def degree(p, diffs=None):
#     """Calculate and return the degree of polynomial p."""
#
#     def get_diffs(l):
#         return [l[i] - l[i-1] for i in range(1, len(l) - 1)]
#
#     # diffs = get_diffs(diffs) if diffs else get_dfs([p(i) for i in range(-11, 12)])
#     if diffs:
#         diffs = get_diffs(diffs)
#     else:
#         diffs = get_diffs([p(i) for i in range(-11, 12)])
#     return 0 if all(not i for i in diffs) else 1 + degree(p, diffs)

# Test inputs
# d0 = lambda x: 1
# d1 = lambda x: x + 1
# d2 = lambda x: x**2 + x + 1
# d3 = lambda x: x**3 + x**2 + x + 1
# d4 = lambda x: x**4
# d5 = lambda x: x**5
# polys = [d0, d1, d2, d3, d4, d5]
#
# # Call and print outputs
# for i, poly in enumerate(polys):
#     print("Expected: {} Actual: {}".format(i, degree(poly)))

# print(fold(tree2, 0, lambda acc, n: acc + n.data))

# bfs(tree2, lambda n: print(n.data))
# def inc(n):
#     n.data += 1
# bfs(tree2, inc)
# bfs(tree2, lambda n: print(n.data))

# print(max_depth(tree))
# print(tree.size())

# def pretty_print(t): # TODO: store last_depth in data, use bfs w/process.
    # n = t
    # if n:
    #     queue = []
    #     queue.append(n)
    #     last_depth = 0
    #     while queue:
    #         n = queue.pop(0)
    #         d = depth(t, n)
    #         print(end="" if d == last_depth else "\n")
    #         print("_" * (max_depth(t) - depth(t, n)), end="")
    #         print(n.data, end="")
    #         last_depth = d
    #         if n.left:
    #             queue.append(n.left)
    #         if n.right:
    #             queue.append(n.right)
    # print()
    # pass
