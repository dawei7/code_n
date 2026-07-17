def solve(allowed: str, words: list[str]) -> int:
    allowed_letters = set(allowed)
    return sum(
        all(character in allowed_letters for character in word)
        for word in words
    )
