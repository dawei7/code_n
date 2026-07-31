def solve(n: int) -> str:
    term = "1"
    for _ in range(n - 1):
        described: list[str] = []
        index = 0
        while index < len(term):
            following = index + 1
            while following < len(term) and term[following] == term[index]:
                following += 1
            described.extend((str(following - index), term[index]))
            index = following
        term = "".join(described)
    return term
