"""Author: Channing J. Hurley
    Module: BinaryTreeUtils -- Defines methods that operate on binary trees, including standard binary tree traversal algorithms.

    TODO:
    
"""

from Tree.BinaryTree import Node

def bfs(n: Node, process=None):
    """Execute an iterative breadth-first (level-order) traversal on a binary tree starting from node n, calling the function "process" on each node.
    """

    assert callable(process) or not process, "process must be callable"
    assert isinstance(n, Node), "Argument must be of type Node or None"

    if n:
        queue = []
        queue.append(n)
        while queue:
            n = queue.pop(0)
            if process:
                process(n)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)


def preorder_dfs(n: Node, process=None):
    """Execute a recursive pre-order depth-first traversal on a binary tree starting at node n, calling the function "process" on each node.
    """

    assert isinstance(n, Node) or n is None, "Argument must be of type Node or None"

    if n:
        if process:
            assert callable(process), "process must be callable"
            process(n)
        preorder_dfs(n.left, process)
        preorder_dfs(n.right, process)


def in_order_dfs(n: Node, process=None):
    """Execute a recursive in-order traversal on a binary tree starting at node n, calling the function "process" on each node.
    """

    assert isinstance(n, Node) or n is None, "Argument must be of type Node or None"

    if n:
        in_order_dfs(n.left, process)
        if process:
            assert callable(process), "process must be callable"
            process(n)
        in_order_dfs(n.right, process)


def postorder_dfs(n: Node, process=None):
    """Execute a recursive post-order traversal on a binary tree starting at node n, calling the function "process" on each node.
    """

    assert isinstance(n, Node) or n is None, "Argument must be of type Node or None"

    if n:
        postorder_dfs(n.left, process)
        postorder_dfs(n.right, process)
        if process:
            assert callable(process), "process must be callable"
            process(n)

'''
def dfs_acc(n: Node, process=None, acc=None):
    """Execute a recursive in-order depth-first traversal of a binary tree, calling the optional function "process" on each node and maintaining an accumulator "acc" to track data throughout recursion
    """

    assert isinstance(n, Node) or n is None, "Argument must be of type Node or None"

    if n:
        in_order_dfs(n.left, process, acc)
        if process:
            assert callable(process), "process must be callable"
            process(n)
        in_order_dfs(n.right, process)
'''

def fold(n, acc, op):
    """"""
    if n:
        new_acc = op(acc, n.data)
        new_acc = fold(n.left, new_acc, op)
        return fold(n.right, new_acc, op)
    else:
        return acc
