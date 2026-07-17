def solve(
    n: int,
    languages: list[list[int]],
    friendships: list[list[int]],
) -> int:
    del n
    known = [set(values) for values in languages]
    affected: set[int] = set()

    for first, second in friendships:
        first -= 1
        second -= 1
        if known[first].isdisjoint(known[second]):
            affected.add(first)
            affected.add(second)

    if not affected:
        return 0

    frequency: dict[int, int] = {}
    for person in affected:
        for language in known[person]:
            frequency[language] = frequency.get(language, 0) + 1

    return len(affected) - max(frequency.values())
