def solve(s: str) -> str:
    result: list[str] = []

    for character in s:
        if len(result) >= 2 and result[-1] == result[-2] == character:
            continue
        result.append(character)

    return "".join(result)
