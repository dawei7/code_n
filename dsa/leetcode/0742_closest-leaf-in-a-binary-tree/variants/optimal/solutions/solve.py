from collections import deque


def solve(root, k: int) -> int:
    parent = {root: None}
    target = None
    stack = [root]

    while stack:
        node = stack.pop()
        if node.val == k:
            target = node
        for child in (node.left, node.right):
            if child is not None:
                parent[child] = node
                stack.append(child)

    queue = deque([target])
    seen = {target}
    while queue:
        node = queue.popleft()
        if node.left is None and node.right is None:
            return node.val
        for neighbor in (node.left, node.right, parent[node]):
            if neighbor is not None and neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
