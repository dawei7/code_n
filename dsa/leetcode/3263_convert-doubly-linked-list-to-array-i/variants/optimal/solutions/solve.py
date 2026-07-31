class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        prev: "Node | None" = None,
        next: "Node | None" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next


def solve(root: Node | None) -> list[int]:
    values = []
    current = root
    while current is not None:
        values.append(current.val)
        current = current.next
    return values
