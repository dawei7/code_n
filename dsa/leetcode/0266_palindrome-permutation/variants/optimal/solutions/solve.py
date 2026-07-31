def solve(s: str) -> bool:
    odd: set[str] = set()
    for character in s:
        if character in odd:
            odd.remove(character)
        else:
            odd.add(character)
    return len(odd) <= 1
