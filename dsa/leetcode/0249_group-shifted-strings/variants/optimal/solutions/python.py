def solve(strings: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}
    for string in strings:
        key = tuple((ord(string[i]) - ord(string[i - 1])) % 26 for i in range(1, len(string)))
        groups.setdefault(key, []).append(string)
    return list(groups.values())
