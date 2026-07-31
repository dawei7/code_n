from collections import Counter


def solve(s: str) -> str:
    counts = Counter(s)

    left_parts = []
    middle = ""
    for index in range(26):
        char = chr(ord("a") + index)
        count = counts[char]
        left_parts.append(char * (count // 2))
        if count % 2:
            middle = char

    left = "".join(left_parts)
    return left + middle + left[::-1]
