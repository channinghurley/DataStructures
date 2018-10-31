"""Test file for tinkering"""

from Tree.BinaryTree import Node
from Tree.Utils import fold as tree_fold
from Tree.Utils import depth
from Tree.Utils import max_depth
from Tree.Utils import find
from Tree.Utils import pretty_print
from List.Utils import fold as list_fold

test = Node(data=1, left=Node(data=1))
tree = Node(Node(Node(data="A"), "B", Node(Node(data="C"), "D", Node(data="E"))), "F", Node(None, "G", Node(Node(data="H"), "I", test)))





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
