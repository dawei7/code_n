def solve(n: int) -> str:
    term = "1"
    for _ in range(n - 1):
        described: list[str] = []
        i = 0
        while i < len(term):
            j = i + 1
            while j < len(term) and term[j] == term[i]:
                j += 1
            described.extend((str(j - i), term[i]))
            i = j
        term = "".join(described)
    return term
