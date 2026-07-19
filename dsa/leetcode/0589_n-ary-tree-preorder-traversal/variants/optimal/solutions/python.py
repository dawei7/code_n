def solve(root) -> list[int]:
    """Return an N-ary tree's root-first, left-to-right preorder."""
    if root is None:
        return []

    traversal: list[int] = []
    stack = [root]
    while stack:
        value, children = stack.pop()
        traversal.append(value)
        stack.extend(reversed(children))

    return traversal

