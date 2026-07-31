def solve(s: str) -> str:
    last_two = s.rfind("2")
    return s[: last_two + 1] if last_two >= 0 else ""
