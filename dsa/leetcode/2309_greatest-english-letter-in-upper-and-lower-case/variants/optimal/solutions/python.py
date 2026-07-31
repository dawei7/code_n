def solve(s: str) -> str:
    present = set(s)
    for code in range(ord("Z"), ord("A") - 1, -1):
        uppercase = chr(code)
        if uppercase in present and uppercase.lower() in present:
            return uppercase
    return ""
