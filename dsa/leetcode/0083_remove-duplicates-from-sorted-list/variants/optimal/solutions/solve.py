class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    current = head
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
