def solve(word1: str, word2: str) -> int:
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    previous = list(range(len(word2) + 1))
    for row, source in enumerate(word1, start=1):
        current = [row]
        for column, target in enumerate(word2, start=1):
            if source == target:
                current.append(previous[column - 1])
            else:
                current.append(
                    1 + min(previous[column], current[-1], previous[column - 1])
                )
        previous = current
    return previous[-1]
