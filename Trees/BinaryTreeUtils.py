""""""

from Trees.BinaryTree import *

def preorder_dfs(tree, process=None):
    """Execute a pre-order depth-first search on a tree, executing the function "process" on each element
    """

    if not isinstance(tree, Leaf):
        if process is not None:
            process(tree.root.data)
        preorder_dfs(tree.root.left, process)
        preorder_dfs(tree.root.right, process)
