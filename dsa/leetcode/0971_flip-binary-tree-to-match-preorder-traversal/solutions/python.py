"""Optimal app-local solution for LeetCode 971."""


def solve(root, voyage):
    flips = []
    index = 0
    stack = [root]

    while stack:
        node = stack.pop()
        if index >= len(voyage) or node.val != voyage[index]:
            return [-1]
        index += 1

        should_flip = (
            node.left is not None
            and index < len(voyage)
            and node.left.val != voyage[index]
        )
        if should_flip:
            flips.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        else:
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    return flips if index == len(voyage) else [-1]
