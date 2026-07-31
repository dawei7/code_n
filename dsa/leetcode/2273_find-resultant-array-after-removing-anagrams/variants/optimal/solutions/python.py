def solve(words: list[str]) -> list[str]:
    result: list[str] = []
    previous_signature: tuple[int, ...] | None = None

    for word in words:
        counts = [0] * 26
        for character in word:
            counts[ord(character) - ord("a")] += 1
        signature = tuple(counts)

        if signature != previous_signature:
            result.append(word)
            previous_signature = signature

    return result
