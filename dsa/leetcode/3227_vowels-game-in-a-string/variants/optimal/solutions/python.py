def solve(s: str) -> bool:
    return any(character in "aeiou" for character in s)
