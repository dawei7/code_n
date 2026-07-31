from collections import deque
from heapq import heappush, heappushpop


def solve(root, k: int) -> int:
    largest = []
    queue = deque([root])

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        if len(largest) < k:
            heappush(largest, level_sum)
        elif level_sum > largest[0]:
            heappushpop(largest, level_sum)

    return largest[0] if len(largest) == k else -1
