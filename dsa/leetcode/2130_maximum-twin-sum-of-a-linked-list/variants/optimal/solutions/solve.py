class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head) -> int:
    slow = head
    fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next

    previous = None
    while slow:
        following = slow.next
        slow.next = previous
        previous = slow
        slow = following

    answer = 0
    first = head
    second = previous
    while second:
        answer = max(answer, first.val + second.val)
        first = first.next
        second = second.next
    return answer
