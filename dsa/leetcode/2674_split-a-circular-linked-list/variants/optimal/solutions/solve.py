class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(list):
    slow = list
    fast = list

    while fast.next != list and fast.next.next != list:
        slow = slow.next
        fast = fast.next.next

    second_head = slow.next
    if fast.next.next == list:
        fast = fast.next

    slow.next = list
    fast.next = second_head
    return [list, second_head]
