def solve(s: str) -> int:
    frequencies = [0] * 26
    for character in s:
        frequencies[ord(character) - ord("a")] += 1
    return sum(1 if frequency % 2 == 1 else 2 for frequency in frequencies if frequency > 0)
