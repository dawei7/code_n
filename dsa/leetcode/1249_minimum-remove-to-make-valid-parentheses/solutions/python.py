def solve(s: str) -> str:
    kept: list[str] = []
    balance = 0
    for char in s:
        if char == "(":
            balance += 1
        elif char == ")":
            if balance == 0:
                continue
            balance -= 1
        kept.append(char)

    result: list[str] = []
    for char in reversed(kept):
        if char == "(" and balance:
            balance -= 1
            continue
        result.append(char)
    return "".join(reversed(result))
