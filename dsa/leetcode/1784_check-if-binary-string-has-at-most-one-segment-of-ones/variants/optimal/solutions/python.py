def solve(s: str) -> bool:
    for index in range(1, len(s)):
        if s[index - 1] == "0" and s[index] == "1":
            return False
    return True
