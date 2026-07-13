from collections import deque


def solve(root) -> list[int]:
    if root is None:
        return []
    queue = deque([root])
    view: list[int] = []
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        view.append(node.val)
    return view
