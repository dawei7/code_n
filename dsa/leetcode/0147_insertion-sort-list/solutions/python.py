from typing import Any


def solve(head: Any | None) -> Any | None:
    dummy = type(head)(0) if head is not None else None
    if dummy is None:
        return None

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
