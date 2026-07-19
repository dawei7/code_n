def solve(s: str, t: str) -> bool:
    positions = [[] for _ in range(10)]
    for index, character in enumerate(s):
        positions[ord(character) - ord("0")].append(index)

    used = [0] * 10
    for character in t:
        digit = ord(character) - ord("0")
        if used[digit] == len(positions[digit]):
            return False

        source_index = positions[digit][used[digit]]
        for smaller in range(digit):
            if (
                used[smaller] < len(positions[smaller])
                and positions[smaller][used[smaller]] < source_index
            ):
                return False

        used[digit] += 1

    return True
