"""Author: Channing J. Hurley


    TODO:
    * update docstring
    * verify recent changes
    * size
    * depth
    * get root
    * in
    * iterative search
    * recursive search
    * insert / __add__
    * delete
    * is_sorted
    * chage __str__ impl to __repr__?
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
        self.set_left(left) # Ensures left's parent is set to self
        self.data = data
        self.set_right(right) # Ensures right's parent is set to self
        self.set_parent(None) # TODO: will this wipe out the parent after set right and left? If not, why not?

    def __repr__(self):
        return "Node({}, {}, {})".format(self.left, self.data, self.right)

    def __str__(self):
        return self.__repr__() # TODO: return more succinct string

    def is_right(self):
        """Return True iff the node is a right child."""
        return self is self.parent.right if self.parent else False

    def is_left(self):
        """Return True iff the node is a left child."""
        return self is self.parent.left if self.parent else False

    def set_parent(self, parent):
        """Assign a refernece to the node's parent, ensuring the parent is of type Node."""
        assert isinstance(parent, Node) or parent is None, "Parent must be of type Node or None"
        self.parent = parent

    def set_right(self, r):
        """Add the node's right child, overridding any existing right child and ensuring the right child is of type Node."""

        assert isinstance(r, Node) or r is None, "Child node must be of type Node or None, instead has type {}".format(type(r))
        self.right = r
        if r: r.set_parent(self) # Do not set the parent of NonTypes

    def set_left(self, l):
        """Add the node's left child, overridding any existing left child and ensuring the left child is of type Node."""
        assert isinstance(l, Node) or l is None, "Child node must be of type Node or None, instead has type {}".format(type(l))
        self.left = l
        if l: l.set_parent(self) # Do not set the parent of NonTypes

    def max_depth(self, depth=-1):
        """Return the depth of the longest branch in the tree, where depth is the number of "edges" from the root to a node. Return zero if the tree is empty."""

        l, r = self.left, self.right
        assert isinstance(l, Node) or not l, "Left child must be Node or None"
        assert isinstance(r, Node) or not r, "Right child must be Node or None"

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
        """Return the number of nodes in the tree"""
        pass
