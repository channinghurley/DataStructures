"""
    TODO
    * docstring
    * verify recent changes
"""

from Trees.Node import Node


class Leaf(Node):
    """"An empty node in a binary tree, i.e. a node with no data and no children ("leaf" node). Extends Node to allow for convenience when implementing recursive methods that operate on Trees and maintain the logic that all subtrees/subnodes within a tree can be themselves considered a tree.
    """

    def __init__(self):
        pass

    def __str__(self):
        return "Leaf"

    def is_empty(self):
        return True
