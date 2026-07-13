from typing import Any


def solve(head_a: Any | None, head_b: Any | None) -> Any | None:
    first = head_a
    second = head_b
    while first is not second:
        first = head_b if first is None else first.next
        second = head_a if second is None else second.next
    return first
