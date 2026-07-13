"""Two-arm iterative postorder for LeetCode 549."""


def solve(root) -> int:
    if root is None:
        return 0

    longest = 1
    # Frame: [node, phase, left_pair, right_pair].
    stack = [[root, 0, None, None]]

    while stack:
        frame = stack[-1]
        node = frame[0]

        if frame[1] == 0:
            frame[1] = 1
            if node.left is not None:
                stack.append([node.left, 0, None, None])
        elif frame[1] == 1:
            frame[1] = 2
            if node.right is not None:
                stack.append([node.right, 0, None, None])
        else:
            increasing = 1
            decreasing = 1

            for child, pair in ((node.left, frame[2]), (node.right, frame[3])):
                if child is None:
                    continue
                child_increasing, child_decreasing = pair
                if child.val == node.val + 1:
                    increasing = max(increasing, child_increasing + 1)
                elif child.val == node.val - 1:
                    decreasing = max(decreasing, child_decreasing + 1)

            longest = max(longest, increasing + decreasing - 1)
            result = (increasing, decreasing)
            stack.pop()

            if stack:
                parent = stack[-1]
                if parent[1] == 1:
                    parent[2] = result
                else:
                    parent[3] = result

    return longest

