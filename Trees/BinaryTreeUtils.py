""""""

from Trees.BinaryTree import *

def bfs(tree: BinaryTree, process=None):
    """Execute an iterative breadth-first (level-order) traversal on a binary tree, calling the function "process" on each node.
    """

    assert callable(process) or not process, "process must be callable"
    assert isinstance(tree, BinaryTree), "Argument must be of type BinaryTree or subtype thereof"

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


def preorder_dfs(tree: BinaryTree, process=None):
    """Execute a recursive pre-order depth-first traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, BinaryTree), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        if process:
            assert callable(process), "process must be callable"
            process(tree.root)
        preorder_dfs(tree.root.left, process)
        preorder_dfs(tree.root.right, process)


def in_order_dfs(tree: BinaryTree, process=None):
    """Execute a recursive in-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, BinaryTree), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        in_order_dfs(tree.root.left, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree.root)
        in_order_dfs(tree.root.right, process)


def postorder_dfs(tree: BinaryTree, process=None):
    """Execute a recursive post-order traversal on a binary tree, calling the function "process" on each node.
    """

    assert isinstance(tree, BinaryTree), "Argument must be of type BinaryTree or subtype thereof"

    if not tree.is_empty():
        postorder_dfs(tree.root.left, process)
        postorder_dfs(tree.root.right, process)
        if process:
            assert callable(process), "process must be callable"
            process(tree.root)
