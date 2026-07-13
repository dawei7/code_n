"""Iterative inorder run counting for LeetCode 501."""


def solve(root) -> list[int]:
    stack = []
    node = root
    has_previous = False
    previous = 0
    run_length = 0
    best_length = 0
    modes: list[int] = []

    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()

        if has_previous and node.val == previous:
            run_length += 1
        else:
            previous = node.val
            has_previous = True
            run_length = 1

        if run_length > best_length:
            best_length = run_length
            modes = [node.val]
        elif run_length == best_length:
            modes.append(node.val)
        node = node.right

    return modes
