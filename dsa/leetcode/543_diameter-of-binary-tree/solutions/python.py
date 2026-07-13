"""One-pass postorder traversal for LeetCode 543."""


def solve(root) -> int:
    if root is None:
        return 0

    diameter = 0
    # Each frame is [node, phase, left_height, right_height].
    stack = [[root, 0, 0, 0]]

    while stack:
        frame = stack[-1]
        node = frame[0]

        if frame[1] == 0:
            frame[1] = 1
            if node.left is not None:
                stack.append([node.left, 0, 0, 0])
        elif frame[1] == 1:
            frame[1] = 2
            if node.right is not None:
                stack.append([node.right, 0, 0, 0])
        else:
            height = 1 + max(frame[2], frame[3])
            diameter = max(diameter, frame[2] + frame[3])
            stack.pop()

            if stack:
                parent = stack[-1]
                if parent[1] == 1:
                    parent[2] = height
                else:
                    parent[3] = height

    return diameter

