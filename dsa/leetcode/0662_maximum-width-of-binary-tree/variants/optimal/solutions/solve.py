from collections import deque


def solve(root) -> int:
    maximum = 0
    queue = deque([(root, 0)])
    while queue:
        level_start = queue[0][1]
        level_end = 0
        for _ in range(len(queue)):
            node, position = queue.popleft()
            position -= level_start
            level_end = position
            if node.left is not None:
                queue.append((node.left, position * 2))
            if node.right is not None:
                queue.append((node.right, position * 2 + 1))
        maximum = max(maximum, level_end + 1)
    return maximum
