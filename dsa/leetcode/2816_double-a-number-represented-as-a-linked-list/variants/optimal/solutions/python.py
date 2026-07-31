def solve(head) -> list[int]:
    values: list[int] = []
    current = head

    if head.val >= 5:
        values.append(1)

    while current:
        digit = (current.val * 2) % 10
        if current.next and current.next.val >= 5:
            digit += 1
        values.append(digit)
        current = current.next

    return values
