"""Optimal app-local solution for LeetCode 1485."""


class Node:
    """Local equivalent of LeetCode's random-pointer binary-tree node."""

    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
        random: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class NodeCopy:
    """Local equivalent of the clone node returned by LeetCode's judge."""

    def __init__(
        self,
        val: int = 0,
        left: "NodeCopy | None" = None,
        right: "NodeCopy | None" = None,
        random: "NodeCopy | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


def solve(root: Node | None) -> NodeCopy | None:
    if root is None:
        return None

    copies = {root: NodeCopy(root.val)}
    stack = [root]

    while stack:
        original = stack.pop()
        copied = copies[original]

        for attribute in ("left", "right", "random"):
            target = getattr(original, attribute)
            if target is None:
                setattr(copied, attribute, None)
                continue

            if target not in copies:
                copies[target] = NodeCopy(target.val)
                stack.append(target)

            setattr(copied, attribute, copies[target])

    return copies[root]
