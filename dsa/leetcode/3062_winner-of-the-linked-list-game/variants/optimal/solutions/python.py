def solve(head) -> str:
    score = 0
    current = head

    while current is not None:
        if current.val > current.next.val:
            score += 1
        else:
            score -= 1
        current = current.next.next

    if score > 0:
        return "Even"
    if score < 0:
        return "Odd"
    return "Tie"
