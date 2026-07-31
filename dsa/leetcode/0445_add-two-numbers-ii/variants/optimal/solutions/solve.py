class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    first = []
    second = []
    while l1 is not None:
        first.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        second.append(l2.val)
        l2 = l2.next

    head = None
    carry = 0
    while first or second or carry:
        total = carry
        if first:
            total += first.pop()
        if second:
            total += second.pop()
        head = ListNode(total % 10, head)
        carry = total // 10
    return head
