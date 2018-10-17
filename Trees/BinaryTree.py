"""Author: Channing J. Hurley
    This module defines the components of a binary tree.

    BinaryTree: The parent class of nodes and leaves that serves as a wrapper for a (potentially arbitrarily nested) node. Implements top-level binary tree functionalities such as insertion, deletion, and searching.

    Leaf (extends BinaryTree): Any empty leaf node of a tree, i.e. a node with no data and no children.

    Node (extends BinaryTree): A node in a binary tree, containing data, a left child, and a right child (each of which could be themselves nodes or leaves).

    TODO:

"""

# from Trees.BinaryTreeUtils import preorder_dfs


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
        self.has_parent = False

    def __str__(self):
        """TODO: recursively print all nodes/leaves"""
        return str(self.root)

    def is_empty(self):
        """Return true if the tree is empty, i.e. contains no nodes."""
        return isinstance(self, Leaf) or self.root is None

    def set_parent(self, parent):
        """Assign a refernce to the root node's parent"""
        self.has_parent = True
        self.parent = parent

    def set_all_parents(self):
        """Ensure all nodes in this tree have a reference to their parent node"""

        def connect(n):
            n.left.set_parent(n)
            n.right.set_parent(n)

        from Trees.BinaryTreeUtils import preorder_dfs
        preorder_dfs(self, connect)

    def is_right(self):
        """Return True iff the tree is a right child. Note: parent must be set"""
        return self is self.parent.right if self.has_parent else False

    def is_left(self):
        """Return True iff the tree is a left child. Note: parent must be set"""
        return not self.is_right() if self.has_parent else False


class Leaf(BinaryTree):
    """"An empty node in a binary tree, i.e. a node with no data and no children ("leaf" node). Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __init__(self):
        BinaryTree.__init__(self) # Do not set root; leaves are not roots

    def __str__(self):
        return "Leaf"


class Node(BinaryTree):
    """A node in a binary tree containing the node data, a right child, a left child, and an optional "pointer" to the parent node. Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and to maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __init__(
        self,
        left: BinaryTree = Leaf(),
        data = None,
        right: BinaryTree = Leaf()
    ):
        # Initialize base class and assign the root of this tree (or subtree) to be the current node
        BinaryTree.__init__(self, root=self)

        assert isinstance(left, BinaryTree), "Left child must be Node or Leaf"
        assert isinstance(right, BinaryTree), "Right child must be Node or Leaf"

        self.left = left
        self.data = data
        self.right = right

    def __str__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def add_right(self, r):
        """Add the node's right child, overridding any existing right children"""
        self.right = r

    def add_left(self, l):
        """Add the node's left child, overridding any existing left children"""
        self.left = l
