def solve(s: str, letter: str) -> int:
    matches = 0
    for character in s:
        if character == letter:
            matches += 1
    return matches * 100 // len(s)
