"""Author: Channing J. Hurley


    TODO:
    * update docstring
    * depth
    * in
    * make data the first arg for convenience
    * iterative search
    * recursive search
    * insert / __add__
    * delete
    * is_sorted
"""


class Node():
    """A node in a binary tree containing the node data, a right child, a left child, and an optional reference to the parent node. Extends BinaryTree to allow for convenience when implementing recursive methods that operate on Trees and to maintain the logic that all subtrees within a tree can be themselves considered a tree.
    """

    def __init__(
        self,
        left=None,
        data=None,
        right=None
    ):
        self.data = data
        self.set_left(left)
        self.set_right(right)
        self.set_parent(None)

    def __str__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def __bool__(self):
        """Return False iff the node is empty, i.e. has no data and no children."""
        return not (self is None or self == Node(None, None, None))

    def __eq__(self, other):
        """Return True iff all attributes of the two nodes are equal."""

        if isinstance(other, Node):
            return (self.data  == other.data and
                    self.left  == other.left and
                    self.right == other.right)
        return False

    def __ne__(self, other):
        return not (self == other)

    def __contains__(self, item):
        """Return True if item is in self, i.e. return True if item is self or item is a subnode of the root node (self).
        """
        from Tree.Utils import find
        return True if find(self, item) else False

    def is_right(self):
        """Return True iff the node is a right child."""
        return self is self.parent.right if self.parent else False

    def is_left(self):
        """Return True iff the node is a left child."""
        return self is self.parent.left if self.parent else False

    def set_parent(self, parent):
        """Assign a refernece to the node's parent, ensuring the parent is of type Node."""

        assert isinstance(parent, Node) or parent is None, "Parent must be of type Node or None, instead has type {}".format(type(parent))

        self.parent = parent

    def set_right(self, r):
        """Add the node's right child, overridding any existing right child and ensuring the right child is of type Node.
        """

        assert isinstance(r, Node) or r is None, "Child node must be of type Node or None, instead has type {}".format(type(r))

        self.right = r
        if r: r.set_parent(self) # Do not set the parent of NonTypes

    def set_left(self, l):
        """Add the node's left child, overridding any existing left child and ensuring the left child is of type Node.
        """

        assert isinstance(l, Node) or l is None, "Child node must be of type Node or None, instead has type {}".format(type(l))

        self.left = l
        if l: l.set_parent(self) # Do not set the parent of NonTypes

    def size(self):
        """Return the number of nodes in the tree starting at root (self)"""
        from Tree.Utils import fold
        return fold(self, 0, lambda acc, n: acc + 1)
