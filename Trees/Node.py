"""Author: Channing J. Hurley
    Module: BinaryTree -- Defines the components of a binary tree.

    Class: BinaryTree -- The parent class of nodes and leaves that serves as a wrapper for a (potentially arbitrarily nested) node. Implements top-level binary tree functionalities such as insertion, deletion, and searching.

    Class: Leaf (extends BinaryTree) -- An empty leaf node of a tree, i.e. a node with no data and no children.

    Class: Node (extends BinaryTree) -- A node in a binary tree, containing data, a left child, and a right child (each of which could be themselves nodes or leaves).

    TODO:
    * move parent logic to node class
    * update docstrings after removal of BinaryTree class
    * verify recent changes
"""

'''
class BinaryTree:
    """Top-level class to serve as parent of BinaryTree and Leaf to maintain the logic that a node consists of data, a left child, and a right child, Leaf is a tree with no data and no children, and that all subtrees within a tree can be themselves considered a tree. This design allows for convenience when implementing recursive methods to operate on trees. This class performs all top-level operations on the overall tree, such as insertion, deletion, and searching and implements members common to both nodes and leaves.

    Notes:
        * References to any data, left children, or right children must be in refernece to a specific node, not the entire tree.
        * root attribute serves as the main accessor/entry point to the tree's data.
    """

    def __init__(self, root=None):
        """Initialize the tree to be empty by default. The tree can also be initialized to a node with data and children. Note: if root is initialized to a node, the root node necessarily extends the BinaryTree class. Root serves as the main accessor of the tree's contents.
        """

        assert root is None or isinstance(root, BinaryTree)
        self.root = root

    def __str__(self):
        """TODO: recursively print all nodes/leaves"""
        return str(self.root)
'''


class Node():
    """A node in a binary tree containing the node data, a right child, a left child, and an optional "pointer" to the parent node. Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and to maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __init__(
        self,
        left=None,
        data=None,
        right=None,
        parent=None
    ):
        # from Trees.Leaf import Leaf

        # assert isinstance(left, Node), "Left child must be Node or Leaf"
        # assert isinstance(right, Node), "Right child must be Node or Leaf"
        # assert isinstance(parent, Node) or not parent, "Parent must be Node or None"

        self.left = left
        self.data = data
        self.right = right
        self.parent = parent

    def __str__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def is_right(self):
        """Return True iff the tree is a right child. Note: parent must be set"""
        return self is self.parent.right if self.parent else False

    def is_left(self):
        """Return True iff the tree is a left child. Note: parent must be set"""
        return self is self.parent.left if self.parent else False

    def set_right(self, r):
        """Add the node's right child, overridding any existing right children"""
        assert isinstance(r, Node), "Child node must be Node or Leaf"
        self.right = r

    def set_left(self, l):
        """Add the node's left child, overridding any existing left children"""
        assert isinstance(l, Node), "Child node must be Node or Leaf"
        self.left = l

    def is_empty(self):
        """Return true if the tree is empty, i.e. contains no nodes and no data."""
        from Trees.Leaf import Leaf
        return self.left is None and self.right is None

    def set_parent(self, parent):
        """Assign a refernece to the node's parent"""
        self.parent = parent

    def set_all_parents(self):
        """Ensure all subnodes of this node have a reference to their parent node"""

        def connect(n):
            n.left.set_parent(n)
            n.right.set_parent(n)

        from Trees.BinaryTreeUtils import preorder_dfs
        preorder_dfs(self, connect)
