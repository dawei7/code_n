"""App-local reference solution for LeetCode 1836."""

from collections import Counter


class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    frequencies = Counter()
    current = head
    while current is not None:
        frequencies[current.val] += 1
        current = current.next

    dummy = ListNode(0, head)
    current = dummy
    while current.next is not None:
        if frequencies[current.next.val] > 1:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
