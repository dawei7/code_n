from collections import Counter


def solve(order: str, s: str) -> str:
    frequencies = Counter(s)
    pieces: list[str] = []
    for character in order:
        pieces.append(character * frequencies.pop(character, 0))
    for character, frequency in frequencies.items():
        pieces.append(character * frequency)
    return "".join(pieces)
