class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    value = 0
    current = head
    while current is not None:
        value = value * 2 + current.val
        current = current.next
    return value
