"""Optimal app-local solution for LeetCode 919."""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.incomplete = deque()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left is None or node.right is None:
                self.incomplete.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def insert(self, val):
        parent = self.incomplete[0]
        node = TreeNode(val)

        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.incomplete.popleft()

        self.incomplete.append(node)
        return parent.val

    def get_root(self):
        return self.root


def _level_order(root):
    values = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while values and values[-1] is None:
        values.pop()
    return values


def solve(root, operations):
    inserter = CBTInserter(root)
    results = []

    for operation in operations:
        if operation[0] == "insert":
            results.append(inserter.insert(operation[1]))
        else:
            results.append(_level_order(inserter.get_root()))

    return results

