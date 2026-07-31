def solve(s: str) -> int:
    smallest = 26
    for character in s:
        if character != "a":
            smallest = min(smallest, ord(character) - ord("a"))
    return 0 if smallest == 26 else 26 - smallest
