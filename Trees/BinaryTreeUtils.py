"""Author: Channing J. Hurley
    Module: BinaryTreeUtils -- Defines methods that operate on binary trees, including standard binary tree traversal algorithms.

    TODO:
    * update variable names (tree)
    * verify recent code changes
"""

from Trees.BinaryTree import *

def bfs(tree: Node, process=None):
    """Execute an iterative breadth-first (level-order) traversal on a binary tree, calling the function "process" on each node.
    """

    assert callable(process) or not process, "process must be callable"
    assert isinstance(tree, Node), "Argument must be of type Node or None"

    if tree:
        queue = []
        queue.append(tree)
        while queue:
            node = queue.pop(0)
            if process:
                process(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def preorder_dfs(tree: Node, process=None):
    """Execute a recursive pre-order depth-first traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node) or tree is None, "Argument must be of type Node or None"

    if tree:
        if process:
            assert callable(process), "process must be callable"
            process(tree)
        preorder_dfs(tree.left, process)
        preorder_dfs(tree.right, process)


def in_order_dfs(tree: Node, process=None):
    """Execute a recursive in-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node) or tree is None, "Argument must be of type Node or None"

    if tree:
        in_order_dfs(tree.left, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree)
        in_order_dfs(tree.right, process)


def postorder_dfs(tree: Node, process=None):
    """Execute a recursive post-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, Node) or tree is None, "Argument must be of type Node or None"

    if tree:
        postorder_dfs(tree.left, process)
        postorder_dfs(tree.right, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree)
