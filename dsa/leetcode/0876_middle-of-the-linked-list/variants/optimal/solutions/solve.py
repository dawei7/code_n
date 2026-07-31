"""Optimal app-local solution for LeetCode 876."""


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
