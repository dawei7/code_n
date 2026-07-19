def solve(s: str, part: str) -> str:
    prefix = [0] * len(part)
    matched = 0
    for index in range(1, len(part)):
        while matched and part[index] != part[matched]:
            matched = prefix[matched - 1]
        if part[index] == part[matched]:
            matched += 1
        prefix[index] = matched

    result: list[str] = []
    states: list[int] = []
    matched = 0
    for character in s:
        while matched and character != part[matched]:
            matched = prefix[matched - 1]
        if character == part[matched]:
            matched += 1

        result.append(character)
        states.append(matched)
        if matched == len(part):
            del result[-len(part):]
            del states[-len(part):]
            matched = states[-1] if states else 0

    return "".join(result)
