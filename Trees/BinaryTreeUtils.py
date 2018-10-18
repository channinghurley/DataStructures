"""Author: Channing J. Hurley
    Module: BinaryTreeUtils -- Defines methods that operate on binary trees, including standard binary tree traversal algorithms.

    TODO:
    * update variable names (tree)
    * verify recent code changes
"""

from Trees.Node import *
from Trees.Leaf import *

def bfs(tree: Node, process=None):
    """Execute an iterative breadth-first (level-order) traversal on a binary tree, calling the function "process" on each node.
    """

    assert callable(process) or not process, "process must be callable"
    assert isinstance(tree, Node), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        queue = []
        queue.append(tree.root)
        while queue:
            node = queue.pop(0)
            if process:
                process(node)
            if not node.left.is_empty():
                queue.append(node.left)
            if not node.right.is_empty():
                queue.append(node.right)


def preorder_dfs(tree: Node, process=None):
    """Execute a recursive pre-order depth-first traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node), "Argument must be of type Node or subtype thereof"

    if not tree.is_empty():
        if process:
            assert callable(process), "process must be callable"
            process(tree)
        preorder_dfs(tree.left, process)
        preorder_dfs(tree.right, process)


def in_order_dfs(tree: Node, process=None):
    """Execute a recursive in-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        in_order_dfs(tree.left, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree)
        in_order_dfs(tree.right, process)


def postorder_dfs(tree: Node, process=None):
    """Execute a recursive post-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        postorder_dfs(tree.left, process)
        postorder_dfs(tree.right, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree)
