"""Author: Channing J. Hurley


    TODO:
    * update docstring
    * depth
    * in
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
        l, r, d = self.left, self.right, self.data
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def __bool__(self):
        """Return False iff the node is empty, i.e. has no data and no children."""
        return not (self is None or self == Node(None, None, None))

    def __eq__(self, other):
        """Return True iff all attributes of the two nodes are equal.

        TODO:
        * verify and cleanup, do not try to get attr's. on NoneTypes
        """
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        else:
            return (self.data  == other.data and
                    self.left  == other.left and
                    self.right == other.right)

    def __ne__(self, other):
        return not (self == other)

    def __contains__(self, item): # TODO
        """Return True if item is in self, i.e. return True if item is self or item is a subnode of the root node (self). If item is not a Node, return True if the data of the root or any of it's subnodes is item."""
        return False

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

    def max_depth(self, depth=-1):
        """Return the depth of the node that is furthest from the root (self), where depth is the number of "edges" from the root to a node. Return zero if the tree is empty.
        TODO: move to utils for a more functional approach, use fold
        """

        l, r = self.left, self.right
        # TODO: remove assertions if they are enforced by setters
        assert isinstance(l, Node) or not l, "Left child must be Node or None, instead has type {}".format(type(l))
        assert isinstance(r, Node) or not r, "Right child must be Node or None, instead has type {}".format(type(r))

        depth += 1
        if l and r:
            return max(l.max_depth(depth), r.max_depth(depth))
        elif l:
            return l.max_depth(depth)
        elif r:
            return r.max_depth(depth)
        else:
            return depth

    def size(self):
        """Return the number of nodes in the tree starting at root (self)"""
        from Tree.Utils import fold
        return fold(self, 0, lambda acc, n: acc + 1)
