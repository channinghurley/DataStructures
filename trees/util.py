"""Author: Channing J. Hurley

    Module: Trees.Util -- Defines utility methods for binary trees.

    Methods:
        * issorted       -- Return True if the tree is sorted (is a BST).
        * bfs            -- Execute a breadth-first (level-order) traversal on a tree.
        * preorder_dfs   -- Execute a pre-order depth-first traversal on a tree.
        * in_order_dfs   -- Execute an in-order depth-first traversal on a tree.
        * post_order_dfs -- Execute a post-order depth-first traversal on a tree.
        * fold           -- Like functools.reduce, but for binary trees instead of lists.
        * find           -- Find a node within a tree.
        * depth          -- Get the depth of a node within a tree.
        * max_depth      -- Get the maximum depth of a binary tree.

    TODO:
        * Make find match on data instead of node itself?
"""

from trees.binary_tree import Node
from operator import gt

def issorted(t, key=gt):
    """Return True if tree t satisfies the binary search property, i.e. for all nodes n in the
    tree, all data contained in the left sub-tree of node n is less or equal to the data of node n,
    and all data contained in the right subtree is greater or equal to the data contained in n. The
    comparison key defaults to the greater than operator, a custom sorting key can be supplied.
    """

    def check_children(acc, n): # FIXME
        """Return True if the immediate children of a node satisfy the binary search property."""
        l, r = n.left, n.right
        if l:
            acc &= l.data <= n.data
        if r:
            acc &= r.data >= n.data
        return acc

    return fold(t, True, check_children)

def bfs(n: Node, process=None):
    """Execute an iterative breadth-first (level-order) traversal on a binary tree starting from
    node n, calling the function "process" on each node.

    Usage:
    >>> bfs(node, lambda n: print(n.data)) # Prints all node data in level-order.
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
    """Recursively "fold" a binary tree, i.e. condense all of the tree's data into one single peice of data that is the result of executing the callable operation "op" on all nodes and accumulating the result in the accumulator "acc", similar to functools.reduce.

    Usage:
    >>> fold(tree, 0, lambda acc, n: acc + n.data) # Return the sum of all data in the tree.
    """

    assert callable(op), "Operation must be callable."

    if n:
        acc = op(acc, n)
        acc = fold(n.left, acc, op)
        return fold(n.right, acc, op)
    else:
        return acc

def find(target, root):
    """Find and return the first node equivalent to node n in tree rooted at root. Return None if
    target is not in root.
    """

    assert isinstance(root, Node), "Argument root must be of type Node."
    assert isinstance(root, Node), "Argument target must be of type Node."
    return fold(root, None, lambda acc, n: n if n == target else acc)

def depth(n, root):
    """Return the depth of node n relative to node root, where depth is the number of edges that must be traversed to get from one node to another. If node n is not in the tree rooted at node root, return -1.
    """

    assert isinstance(n, Node), "Argument n must be of type Node."
    assert isinstance(root, Node), "Argument root must be of Type Node."

    n = find(n, root) # point n to the equivalent node within the tree

    if n:
        if n is root:
            return 0
        else:
            return depth(n.parent, root) + 1
    else:
        return -1

def max_depth(t):
    """Return the maximum depth of tree t, i.e. the depth of the node with the greatest depth
    relative to node t.
    """

    assert isinstance(t, Node), "Argument must be of type Node."
    return fold(t, 0, lambda acc, n: max(acc, depth(n, t)))
