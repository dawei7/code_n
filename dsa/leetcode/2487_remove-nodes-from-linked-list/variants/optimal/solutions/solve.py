class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> ListNode | None:
    reversed_head = None
    current = head
    while current:
        following = current.next
        current.next = reversed_head
        reversed_head = current
        current = following

    maximum = 0
    kept_head = None
    current = reversed_head
    while current:
        following = current.next
        if current.val >= maximum:
            maximum = current.val
            current.next = kept_head
            kept_head = current
        current = following

    return kept_head
