"""File for tinkering"""

from Trees.BinaryTree import Node
from Trees.Util import *
from Lists.Util import fold as list_fold

test = Node(data=1, left=Node(data=1))
tree = Node(Node(Node(data="A"), "B", Node(Node(data="C"), "D", Node(data="E"))), "F", Node(None, "G", Node(Node(data="H"), "I")))

tree2 = Node(Node(Node(data=4), 2, Node(data=5)), 1, Node(Node(data=6), 3, Node(data=7)))

# total = 0
# def sum(n):
#     global total
#     total += n.data
#
# bfs(tree2, sum)
# bfs(tree2, lambda n: print(n.data))
# print("total:", total)

# print(fold(tree2, 0, lambda acc, n: acc + n.data))

# bfs(tree2, lambda n: print(n.data))
def inc(n):
    n.data += 1
# bfs(tree2, inc)
# bfs(tree2, lambda n: print(n.data))

# print(max_depth(tree))
print(tree.size())

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
