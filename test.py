from Trees.BinaryTree import *

# t = Node(1)
# print(isinstance(t, BinaryTree))
# print(t)
# print(t.left)

# t = BinaryTree(root=Node(1, Leaf(), Leaf()))
# print(t)

n4 = Node(Leaf(), 4, Leaf())
n3 = Node(n4, 3, n4)
n2 = Node(n3, 2, n3)
r = Node(n2, 1, n2)

# print(r)

ptr = r

def pretty_print(n): # FIXME
    def helper(n, depth=0):
        if not isinstance(n, Leaf):
            print("   " * depth, n.data)
            helper(n.left, depth + 1)
            helper(n.right, depth + 1)
    helper(n)

pretty_print(r)
