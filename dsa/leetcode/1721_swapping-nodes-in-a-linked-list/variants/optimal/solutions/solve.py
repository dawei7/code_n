class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head, k: int):
    kth_from_start = head
    for _ in range(k - 1):
        kth_from_start = kth_from_start.next

    kth_from_end = head
    runner = kth_from_start
    while runner.next is not None:
        runner = runner.next
        kth_from_end = kth_from_end.next

    kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
    return head
