from typing import Any


def solve(head: Any | None) -> int:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return -1

    entry = head
    index = 0
    while entry is not slow:
        entry = entry.next
        slow = slow.next
        index += 1
    return index
