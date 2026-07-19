from typing import Any


def _split(head: Any | None, width: int) -> Any | None:
    if head is None:
        return None
    for _ in range(1, width):
        if head.next is None:
            break
        head = head.next
    following = head.next
    head.next = None
    return following


def _merge(left: Any | None, right: Any | None, dummy: Any) -> tuple[Any, Any]:
    tail = dummy
    while left is not None and right is not None:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left is not None else right
    while tail.next is not None:
        tail = tail.next
    return dummy.next, tail


def solve(head: Any | None) -> Any | None:
    if head is None or head.next is None:
        return head

    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next

    dummy = type(head)(0)
    dummy.next = head
    width = 1
    while width < length:
        previous = dummy
        current = dummy.next
        while current is not None:
            left = current
            right = _split(left, width)
            current = _split(right, width)
            merged_head, merged_tail = _merge(left, right, type(head)(0))
            previous.next = merged_head
            previous = merged_tail
        width *= 2
    return dummy.next
