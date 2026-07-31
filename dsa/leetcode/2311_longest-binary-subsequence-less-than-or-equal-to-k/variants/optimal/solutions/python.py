def solve(s: str, k: int) -> int:
    value = 0
    place = 1
    length = 0

    for bit in reversed(s):
        if bit == "0":
            length += 1
            place <<= 1
        elif value + place <= k:
            value += place
            length += 1
            place <<= 1

    return length
