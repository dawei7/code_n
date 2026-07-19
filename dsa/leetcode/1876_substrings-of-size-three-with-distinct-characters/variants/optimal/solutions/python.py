def solve(s: str) -> int:
    return sum(
        s[index] != s[index + 1]
        and s[index] != s[index + 2]
        and s[index + 1] != s[index + 2]
        for index in range(len(s) - 2)
    )
