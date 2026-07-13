def solve(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}
    for word in strs:
        counts = [0] * 26
        for character in word:
            counts[ord(character) - ord("a")] += 1
        key = tuple(counts)
        groups.setdefault(key, []).append(word)
    return list(groups.values())
