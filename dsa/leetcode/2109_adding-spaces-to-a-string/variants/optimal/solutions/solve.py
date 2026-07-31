def solve(s: str, spaces: list[int]) -> str:
    parts: list[str] = []
    previous = 0

    for index in spaces:
        parts.append(s[previous:index])
        parts.append(" ")
        previous = index

    parts.append(s[previous:])
    return "".join(parts)
