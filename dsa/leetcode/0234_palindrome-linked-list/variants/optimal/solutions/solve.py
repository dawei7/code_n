class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    previous = None
    current = slow
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following

    left, right = head, previous
    palindrome = True
    while right is not None:
        if left.val != right.val:
            palindrome = False
            break
        left = left.next
        right = right.next

    current, previous = previous, None
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return palindrome
