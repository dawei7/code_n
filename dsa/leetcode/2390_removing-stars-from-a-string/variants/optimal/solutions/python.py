def solve(s: str) -> str:
    remaining: list[str] = []

    for character in s:
        if character == "*":
            remaining.pop()
        else:
            remaining.append(character)

    return "".join(remaining)
