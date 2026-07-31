def solve(s: str, repeatLimit: int) -> str:
    counts = [0] * 26
    for character in s:
        counts[ord(character) - ord("a")] += 1

    pieces = []
    largest = 25

    while largest >= 0:
        if counts[largest] == 0:
            largest -= 1
            continue

        take = min(counts[largest], repeatLimit)
        pieces.append(chr(ord("a") + largest) * take)
        counts[largest] -= take

        if counts[largest] == 0:
            continue

        separator = largest - 1
        while separator >= 0 and counts[separator] == 0:
            separator -= 1
        if separator < 0:
            break

        pieces.append(chr(ord("a") + separator))
        counts[separator] -= 1

    return "".join(pieces)
