def solve(s: str) -> str:
    length = len(s)
    removable = [[False] * (length + 1) for _ in range(length + 1)]
    for index in range(length + 1):
        removable[index][index] = True

    for interval_length in range(2, length + 1, 2):
        for left in range(length - interval_length + 1):
            right = left + interval_length
            for partner in range(left + 1, right, 2):
                consecutive = abs(ord(s[left]) - ord(s[partner])) in (1, 25)
                if consecutive and removable[left + 1][partner] and removable[partner + 1][right]:
                    removable[left][right] = True
                    break

    best = [""] * (length + 1)
    for left in range(length - 1, -1, -1):
        if removable[left][length]:
            continue
        best[left] = min(
            s[survivor] + best[survivor + 1] for survivor in range(left, length) if removable[left][survivor]
        )

    return best[0]
