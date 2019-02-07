"""Author: Channing J. Hurley

    Module: Trees.BinarySearchTree -- Extends BinaryTree.Node and adds the enforcement that the tree is sorted.

    TODO:
        * Insert method
        * edit ctor to use insert so created in order
        * bst is sorted to util
        * delete and shift method
        * Can we build off of instances of Node? Does this cause any issues?
            - subtrees will not have insert method
"""

from trees.binary_tree import Node

class Bst(Node):
    """"""

    def __init__(self, data=None, left=None, right=None):
        super().__init__(data, left, right)

    @classmethod
    def from_list(cls, seq):
        """Factory method to create a BST from a sequence by constructing a new BST and calling
        insert on the BST for each element in the sequence, which will maintain the binary search
        poperty.
        """

        it = iter(seq) # TODO: Catch TypeError?
        root = cls(next(it))
        for elem in it:
            root.insert(cls(elem))
        return root

    def insert(self, n):
        """Insert a node into the BST at a location that will maintain the binary search property
        within the BST; i.e. the key in each node must be greater than or equal to the key stored
        in any node in the left sub-tree, and less than or equal to an key stored in the right
        sub-tree.
        """

        if n.data > self.data:
            if self.right:
                self.right.insert(n)
            else:
                self.set_right(n)
        else:
            if self.left:
                self.left.insert(n)
            else:
                self.set_left(n)
