class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head, left: int, right: int):
    before = None
    current = head
    for _ in range(1, left):
        before = current
        current = current.next

    segment_tail = current
    previous = None
    for _ in range(right - left + 1):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    segment_tail.next = current
    if before is None:
        return previous
    before.next = previous
    return head
