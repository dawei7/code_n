def solve(words1: list[str], words2: list[str]) -> int:
    counts1: dict[str, int] = {}
    counts2: dict[str, int] = {}

    for word in words1:
        counts1[word] = counts1.get(word, 0) + 1

    for word in words2:
        counts2[word] = counts2.get(word, 0) + 1

    return sum(
        count == 1 and counts2.get(word) == 1
        for word, count in counts1.items()
    )
