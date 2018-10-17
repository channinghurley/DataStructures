"""Test file for tinkering"""

from Trees.BinaryTree import *
from Trees.BinaryTreeUtils import *

# t = Node(1)
# print(isinstance(t, BinaryTree))
# print(t)
# print(t.left)

# t = BinaryTree(root=Node(1, Leaf(), Leaf()))
# print(t)

# n4 = Node(Leaf(), 4, Leaf())
# n3 = Node(n4, 3, Leaf())
# n2 = Node(n3, 2, Leaf())
# r = Node(n2, 1, Leaf())
# n4.parent = n3
# n3.parent = n2
# n2.parent = r

# print(r)

# def pretty_print(n):
#     def helper(n, depth=0):
#         if not isinstance(n, Leaf):
#             for i in range(depth - 1):
#                 print("|  ", end='')
#             print("+--" if depth else "", n.root.data, sep='')
#             helper(n.root.left, depth + 1)
#             # print("|  " * depth)
#             helper(n.root.right, depth + 1)
#     helper(n)


# tree = BinaryTree(root=Node())
# root = tree.root
# root.data = 2
#
# left = Node(data=1)
# right = Node(data=3)
# root.add_left(left)
# root.add_right(right)
# left.set_parent(root)
# right.set_parent(root)
#
# print(tree)
# print(root.isright())
# print(root.isleft())
# print(left.isleft())
# print(right.isright())
# pretty_print(tree)


tree = BinaryTree(root=Node(Node(Node(data="A"), "B", Node(Node(data="C"), "D", Node(data="E"))), "F", Node(Leaf(), "G", Node(Node(data="H"), "I", Leaf()))))

bfs(tree, lambda n: print(n.data, "has parent: ", n.has_parent))

# def set_all_parents(n):
#     n.left.set_parent(n)
#     n.right.set_parent(n)
#
# preorder_dfs(tree, set_all_parents)

tree.set_all_parents()

bfs(tree, lambda n: print(n.data, "Parent: ", n.parent.data if n.has_parent else None))

# print("Pre-order: ", end="")
# preorder_dfs(tree, l)
# print()
# print("In-order: ", end="")
# in_order_dfs(tree, l)
# print()
# print("Post-order: ", end="")
# postorder_dfs(tree, l)
# print()
#
# preorder_dfs(BinaryTree(), l)
# preorder_dfs(Leaf(), l)
