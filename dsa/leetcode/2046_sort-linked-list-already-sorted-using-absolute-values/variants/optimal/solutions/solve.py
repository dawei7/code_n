class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    current = head

    while current.next is not None:
        if current.next.val < 0:
            moved = current.next
            current.next = moved.next
            moved.next = head
            head = moved
        else:
            current = current.next

    return head
