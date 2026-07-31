class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    dummy = ListNode(0, head)
    slow = dummy
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next
    return dummy.next
