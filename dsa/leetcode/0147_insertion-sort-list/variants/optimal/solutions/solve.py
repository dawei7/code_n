class ListNode:
    """Local equivalent of the linked-list node supplied by LeetCode's judge."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    dummy = ListNode()
    current = head
    while current is not None:
        following = current.next
        position = dummy
        while position.next is not None and position.next.val <= current.val:
            position = position.next
        current.next = position.next
        position.next = current
        current = following
    return dummy.next
