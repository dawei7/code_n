class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None) -> int:
    stack: list[TreeNode] = []
    current = root
    previous: int | None = None
    best = float("inf")

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if previous is not None:
            best = min(best, current.val - previous)
        previous = current.val
        current = current.right

    return int(best)
