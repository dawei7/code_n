"""Optimal app-local round-trip codec for LeetCode 431."""

from types import SimpleNamespace


def solve(tree):
    def encode(node):
        if node is None:
            return None
        value, children = node
        binary = SimpleNamespace(val=value, left=None, right=None)
        previous = None
        for child in children:
            encoded_child = encode(child)
            if previous is None:
                binary.left = encoded_child
            else:
                previous.right = encoded_child
            previous = encoded_child
        return binary

    def decode(binary):
        if binary is None:
            return None
        children = []
        child = binary.left
        while child is not None:
            children.append(decode(child))
            child = child.right
        return [binary.val, children]

    return decode(encode(tree))
