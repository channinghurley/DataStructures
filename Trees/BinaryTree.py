"""Author: Channing J. Hurley
    This module defines the components of a binary tree.

    BinaryTree: The parent class of nodes and leaves that serves as a wrapper for a (potentially arbitrarily nested) node. Implements top-level binary tree functionalities such as insertion, deletion, and searching.

    Leaf (extends BinaryTree): Any empty leaf node of a tree, i.e. a node with no data and no children.

    Node (extends BinaryTree): A node in a binary tree, containing data, a left child and a right child (each of which could be leaves).

    TODO:

"""


class BinaryTree:
    """Top-level class to serve as parent of BinaryTree and Empty to maintain the logic that a node consists of data, a left child, and a right child, Leaf is a tree with no data and no children, and that all subtrees within a tree can be themselves considered a tree. This design allows for convenience when implementing recursive methods to operate on trees. This class performs all top-level operations on the overall tree, such as insertion, deletion, and searching.
    """

    def __init__(self, root=None):
        """Initialize the tree to be empty by default. The tree can also be initialized to a node with data and children. Note: if root is initialized to a node, the root node extends the BinaryTree class.
        """
        assert root is None or isinstance(root, BinaryTree)
        self.root = root

    def __str__(self):
        """TODO: recursively print all nodes/leaves"""
        return str(self.root)


class Leaf(BinaryTree):
    """"An empty node in a binary tree, i.e. a node with no data and no children ("leaf" node). Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __str__(self):
        return "Leaf"


class Node(BinaryTree):
    """A node in a binary tree containing the node data, a right child, and a left child. Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and to maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __init__(
        self,
        left: BinaryTree=Leaf(),
        data=None,
        right: BinaryTree=Leaf()
    ):

        assert isinstance(left, BinaryTree)
        assert isinstance(right, BinaryTree)

        self.left = left
        self.data = data
        self.right = right

    def __str__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)
