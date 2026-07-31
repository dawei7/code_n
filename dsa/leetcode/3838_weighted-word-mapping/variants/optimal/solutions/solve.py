def solve(words: list[str], weights: list[int]) -> str:
    mapped: list[str] = []

    for word in words:
        total = 0
        for character in word:
            total += weights[ord(character) - ord("a")]
        mapped.append(chr(ord("z") - total % 26))

    return "".join(mapped)
