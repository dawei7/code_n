def solve(s: str) -> int:
    present = 0
    for character in s:
        present |= 1 << ord(character) - ord("a")
    return present.bit_count()
