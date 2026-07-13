from typing import Any


def solve(head: Any | None) -> None:
    if head is None or head.next is None:
        return

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None
    previous = None
    while second is not None:
        following = second.next
        second.next = previous
        previous = second
        second = following

    first = head
    second = previous
    while second is not None:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next
