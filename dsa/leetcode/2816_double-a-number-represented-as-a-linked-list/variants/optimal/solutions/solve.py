class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> ListNode | None:
    if head.val >= 5:
        head = ListNode(0, head)

    current = head
    while current:
        current.val = (current.val * 2) % 10
        if current.next and current.next.val >= 5:
            current.val += 1
        current = current.next

    return head
