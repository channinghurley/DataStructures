"""Test file for tinkering"""

from Tree.BinaryTree import Node
from Tree.Utils import fold as tree_fold
from List.Utils import fold as list_fold

tree = Node(Node(Node(data="A"), "B", Node(Node(data="C"), "D", Node(data="E"))), "F", Node(None, "G", Node(Node(data="H"), "I", None)))

# l = [1, 2, 3, 4, 5]
#
# print(list_fold(l, 0, lambda acc, x: acc - x))
#
t = Node(Node(Node(data=10), 10, Node(data=11)), 1111, Node(Node(data=113), 13, Node(data=14)))
print(t)
print(tree_fold(t, 0, lambda acc, x: acc + x))
print(t.size())


# def l(n: Node, acc=0):
#     print(n.data)

# preorder_dfs(tree, lambda n: print(n.data, end=" "), 0)
# print()

# print(tree)
# print(tree.max_depth())
#
# tree = Node(Node(), 1, Node())
# print(tree)
# print(tree.max_depth())
#
# # t2 = Node(Node(None, None, None), 1, Node(None, None, None))
# #
# # print(t2)
#
# def view_parents(n):
#     pd = n.parent
#     if n.parent:
#         pd = n.parent.data
#     s = "{}: Parent = {}".format(n.data, pd, sep=" ")
#     print(s)

# in_order_dfs(tree, view_parents)

# print(tree == tree)
# n1 = Node(Node(Node(data=2), 4, Node()), 1, Node(data=3))
# n2 = Node(Node(Node(data=2), 4, Node()), 1, Node(data=3))
# print(n1)
# print(n1==n2)
# print(n1!=n2)
# print(n2 in n1)

# in_order_dfs(tree, view_parents)
# Output:
# A: Parent = B
# B: Parent = F
# C: Parent = D
# D: Parent = B
# E: Parent = D
# F: Parent = None
# G: Parent = F
# H: Parent = I
# I: Parent = G



# n = Node(Node(data=1), 2, Node(data=3))
# preorder_dfs(n)
#
# print(n.data)
# print(n.left)
# print(n.right)
# print(n.parent)
# print(n.left.parent)
# print(n.right.parent)
# n.set_all_parents()
# print(n.parent)
# print(n.left.parent)
# print(n.right.parent)
# print(n.left.parent is n.right.parent)
# print(n.left.is_left())
# print(n.right.is_right())



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



'''


bfs(tree, lambda n: print(n.data, "has parent: ", n.has_parent))

# def set_all_parents(n):
#     n.left.set_parent(n)
#     n.right.set_parent(n)
#
# preorder_dfs(tree, set_all_parents)

tree.set_all_parents()

bfs(tree, lambda n: print(n.data, "Parent: ", n.parent.data if n.has_parent else None))
'''
# l = lambda n: print(n.data, end=" ")
# print("Pre-order: ", end="")
# preorder_dfs(tree, l)
# print()
# print("In-order: ", end="")
# in_order_dfs(tree, l)
# print()
# print("Post-order: ", end="")
# postorder_dfs(tree, l)
# print()
# print("Level-order: ", end="")
# bfs(tree, l)
# print()
#
# preorder_dfs(BinaryTree(), l)
# preorder_dfs(Leaf(), l)
