from collections import deque


def solve(root, target_path: str):
    target = root
    for direction in target_path:
        target = target.left if direction == "L" else target.right

    queue = deque([root])
    while queue:
        level_size = len(queue)
        for index in range(level_size):
            node = queue.popleft()
            if node is target:
                return queue[0] if index + 1 < level_size else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return None
