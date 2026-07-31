def solve(s: str) -> str:
    seen = 0
    for character in s:
        bit = 1 << (ord(character) - ord("a"))
        if seen & bit:
            return character
        seen |= bit
    return ""
