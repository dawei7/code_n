def solve(s: str) -> int:
    two_before = 1
    one_before = 0 if s[0] == "0" else 1
    for index in range(1, len(s)):
        current = one_before if s[index] != "0" else 0
        if 10 <= int(s[index - 1 : index + 1]) <= 26:
            current += two_before
        two_before, one_before = one_before, current
    return one_before
