class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(nums: list[int], head: ListNode | None) -> ListNode | None:
    removed = set(nums)
    dummy = ListNode(0, head)
    previous = dummy
    current = head

    while current:
        if current.val in removed:
            previous.next = current.next
        else:
            previous = current
        current = current.next

    return dummy.next
