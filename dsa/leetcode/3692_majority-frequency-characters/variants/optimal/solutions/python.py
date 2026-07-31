from collections import Counter, defaultdict


def solve(s: str) -> str:
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for character, frequency in Counter(s).items():
        groups[frequency].append(character)
    return "".join(
        max(
            groups.items(),
            key=lambda item: (len(item[1]), item[0]),
        )[1]
    )
