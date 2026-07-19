def solve(word: str) -> int:
    total = len(word)
    previous = "a"

    for character in word:
        direct = abs(ord(character) - ord(previous))
        total += min(direct, 26 - direct)
        previous = character

    return total
