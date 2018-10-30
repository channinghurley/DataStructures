"""Author: Channing J. Hurley
    Module: BinaryTreeUtils -- Defines methods that operate on binary trees, including standard binary tree traversal algorithms.

    TODO:
    * pre/post/in order fold
    * add assertions to depth methods to enusre nodes
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

def fold(n, acc, op):
    """Recursively "fold" a binary tree, i.e. condense all of the tree's data into one single peice of data that is the result of executing the callable operation "op" on all nodes and accumulating the result in the accumulator "acc".

    TODO:
    * fix so that op does not necessarily perform on data; update docstrign accordingly
    """

    assert callable(op), "Operation must be callable."

    if n:
        acc = op(acc, n)
        acc = fold(n.left, acc, op)
        return fold(n.right, acc, op)
    else:
        return acc

def find(root, target):
    """Find and return the first node equivalent to node n in tree rooted at root. Return None if target is not in root."""
    assert isinstance(root, Node), "Argument root must be of type Node."
    assert isinstance(root, Node), "Argument target must be of type Node."
    return fold(root, None, lambda acc, n: n if n == target else acc)

def depth(root, n):
    """Return the depth of node n relative to node root, where depth is the number of edges that must be traversed to get from one node to another. If node n is not in the tree rooted at node root, return -1.
    """

    assert isinstance(root, Node), "Argument root must be of Type Node."
    assert isinstance(n, Node), "Argument n must be of type Node."

    n = find(root, n) # point n to the equivalent node within the tree

    if n:
        if n is root:
            return 0
        else:
            return depth(root, n.parent) + 1
    else:
        return -1

def max_depth(t):
    """Return the maximum depth of tree t, i.e. the depth of the node with the greatest depth relative to node t."""
    assert isinstance(t, Node), "Argument must be of type Node."
    return fold(t, 0, lambda acc, n: max(acc, depth(t, n)))

def pretty_print(t):
    """Prett-print a binary tree."""
    pass
