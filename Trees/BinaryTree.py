"""Author: Channing J. Hurley


    TODO:
    * update docstrings after removal of BinaryTree class
    * verify recent changes
    * remove is_empty function
    * insert
    * delete
    * is_sorted
"""


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
        self.left = left
        self.data = data
        self.right = right
        self.parent = parent

    def __str__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def is_right(self):
        """Return True iff the tree is a right child."""
        return self is self.parent.right if self.parent else False

    def is_left(self):
        """Return True iff the tree is a left child."""
        return self is self.parent.left if self.parent else False

    def set_right(self, r):
        """Add the node's right child, overridding any existing right children"""
        assert isinstance(r, Node), "Child node must be Node or Leaf"
        self.right = r

    def set_left(self, l):
        """Add the node's left child, overridding any existing left children"""
        assert isinstance(l, Node), "Child node must be Node or Leaf"
        self.left = l

    ''' TODO: remove
    def is_empty(self):
        """Return true if the tree is empty, i.e. contains no nodes and no data."""
        return self.left is None and self.right is None
    '''

    def set_parent(self, parent):
        """Assign a refernece to the node's parent"""
        self.parent = parent

    def set_all_parents(self):
        """Ensure all subnodes of this node have a reference to their parent node"""

        def connect(n):
            if n.left:
                n.left.set_parent(n)
            if n.right:
                n.right.set_parent(n)

        from Trees.BinaryTreeUtils import preorder_dfs
        preorder_dfs(self, connect)
