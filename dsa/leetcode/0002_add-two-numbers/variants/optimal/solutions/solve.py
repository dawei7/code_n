class ListNode:
    """Local equivalent of the linked-list node supplied by LeetCode's judge."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    dummy = ListNode()
    tail = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:
        left = l1.val if l1 is not None else 0
        right = l2.val if l2 is not None else 0
        carry, digit = divmod(left + right + carry, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    return dummy.next
