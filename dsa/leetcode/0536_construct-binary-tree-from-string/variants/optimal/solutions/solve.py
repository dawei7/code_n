class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(s: str) -> TreeNode | None:
    if not s:
        return None

    stack = []
    root = None
    cursor = 0
    while cursor < len(s):
        character = s[cursor]
        if character == "(":
            if cursor + 1 < len(s) and s[cursor + 1] == ")":
                stack[-1][1] += 1
                cursor += 2
            else:
                cursor += 1
            continue
        if character == ")":
            stack.pop()
            cursor += 1
            continue

        start = cursor
        if s[cursor] == "-":
            cursor += 1
        while cursor < len(s) and s[cursor].isdigit():
            cursor += 1
        node = TreeNode(int(s[start:cursor]))
        if stack:
            parent, slot = stack[-1]
            if slot == 0:
                parent.left = node
            else:
                parent.right = node
            stack[-1][1] += 1
        else:
            root = node
        stack.append([node, 0])

    return root
