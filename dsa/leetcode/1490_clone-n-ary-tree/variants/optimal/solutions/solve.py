class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(self, val: int = 0, children: "list[Node] | None" = None):
        self.val = val
        self.children = [] if children is None else children


def solve(root: Node | None) -> Node | None:
    if root is None:
        return None

    cloned_root = Node(root.val, [])
    stack = [(root, cloned_root)]

    while stack:
        original, cloned = stack.pop()
        for child in original.children:
            child_clone = Node(child.val, [])
            cloned.children.append(child_clone)
            stack.append((child, child_clone))

    return cloned_root
