from math import gcd


def solve(head) -> list[int]:
    values: list[int] = []
    current = head

    while current.next:
        values.append(current.val)
        values.append(gcd(current.val, current.next.val))
        current = current.next

    values.append(current.val)
    return values
