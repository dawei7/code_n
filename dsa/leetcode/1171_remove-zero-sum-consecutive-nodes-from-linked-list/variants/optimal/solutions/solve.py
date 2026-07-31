class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    dummy = ListNode(0, head)
    last = {}
    prefix = 0
    current = dummy

    while current is not None:
        prefix += current.val
        last[prefix] = current
        current = current.next

    prefix = 0
    current = dummy
    while current is not None:
        prefix += current.val
        current.next = last[prefix].next
        current = current.next

    return dummy.next
