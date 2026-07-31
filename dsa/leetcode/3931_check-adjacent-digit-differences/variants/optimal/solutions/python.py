def solve(s: str) -> bool:
    for left, right in zip(s, s[1:]):
        if abs(ord(left) - ord(right)) > 2:
            return False
    return True
