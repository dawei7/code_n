def solve(root) -> list[int]:
    """Return an N-ary tree's left-to-right postorder."""
    if root is None:
        return []

    reversed_postorder: list[int] = []
    stack = [root]
    while stack:
        value, children = stack.pop()
        reversed_postorder.append(value)
        stack.extend(children)

    reversed_postorder.reverse()
    return reversed_postorder

