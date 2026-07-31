class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(headA: ListNode | None, headB: ListNode | None) -> ListNode | None:
    first = headA
    second = headB
    while first is not second:
        first = headB if first is None else first.next
        second = headA if second is None else second.next
    return first
