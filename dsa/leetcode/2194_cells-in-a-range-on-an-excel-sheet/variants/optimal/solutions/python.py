def solve(s: str) -> list[str]:
    return [
        f"{chr(column)}{row}"
        for column in range(ord(s[0]), ord(s[3]) + 1)
        for row in range(int(s[1]), int(s[4]) + 1)
    ]
