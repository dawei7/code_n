"""Level-order traversal for LeetCode 513."""

from collections import deque


def solve(root) -> int:
    queue = deque([root])
    answer = root.val
    while queue:
        answer = queue[0].val
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return answer
