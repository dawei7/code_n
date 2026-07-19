"""Optimal app-local solution for LeetCode 1305."""


def _inorder(root):
    values = []
    stack = []
    node = root

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        values.append(node.val)
        node = node.right

    return values


def solve(root1, root2):
    first = _inorder(root1)
    second = _inorder(root2)
    merged = []
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged
