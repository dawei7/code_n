from math import gcd


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> ListNode | None:
    current = head
    while current.next:
        current.next = ListNode(gcd(current.val, current.next.val), current.next)
        current = current.next.next
    return head
