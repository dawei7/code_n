"""One-pass iterative postorder for LeetCode 563."""


def solve(root) -> int:
    if root is None:
        return 0

    total_tilt = 0
    # Frame: [node, phase, left_sum, right_sum].
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
            total_tilt += abs(frame[2] - frame[3])
            subtree_sum = node.val + frame[2] + frame[3]
            stack.pop()

            if stack:
                parent = stack[-1]
                if parent[1] == 1:
                    parent[2] = subtree_sum
                else:
                    parent[3] = subtree_sum

    return total_tilt

