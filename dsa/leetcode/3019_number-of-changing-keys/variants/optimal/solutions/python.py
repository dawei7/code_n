def solve(s: str) -> int:
    return sum(
        s[index - 1].lower() != s[index].lower()
        for index in range(1, len(s))
    )
