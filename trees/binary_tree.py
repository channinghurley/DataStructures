"""Author: Channing J. Hurley

    Module: Trees.BinaryTree -- Defines the Node class, which makes up the structure of a binary tree.

    Notes:
        * This is not necessarily a binary search tree as this class itself enforces no node order.

    TODO:
        * update docstring
        * make data the first arg for convenience (construct nodes Node(1) for example)
        * pretty_print -- current str should be repr
"""


class Node():
    """A node in a binary tree consisting of data, a left child, a right child, and an optional parent node. The children and parent are themselves instances of the Node class (if they exist) For added functionality, use the Trees.Util methods.
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
        return not self == Node(None, None, None)

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
        from trees.util import find
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
        """Return the number of nodes in the tree starting at root (self)."""
        from trees.util import fold
        return fold(self, 0, lambda acc, n: acc + 1)
