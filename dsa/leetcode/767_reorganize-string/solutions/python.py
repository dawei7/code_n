from collections import Counter


def solve(s: str) -> str:
    frequencies = Counter(s)
    if max(frequencies.values()) > (len(s) + 1) // 2:
        return ""

    result = [""] * len(s)
    position = 0
    for character, count in sorted(frequencies.items(), key=lambda item: -item[1]):
        for _ in range(count):
            if position >= len(s):
                position = 1
            result[position] = character
            position += 2

    return "".join(result)
