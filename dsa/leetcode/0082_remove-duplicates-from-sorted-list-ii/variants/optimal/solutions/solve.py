class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    result_head = None
    result_tail = None
    current = head

    while current is not None:
        run_start = current
        while current.next is not None and current.next.val == current.val:
            current = current.next
        next_run = current.next
        if run_start is current:
            if result_head is None:
                result_head = run_start
            else:
                result_tail.next = run_start
            result_tail = run_start
        current = next_run

    if result_tail is not None:
        result_tail.next = None
    return result_head
