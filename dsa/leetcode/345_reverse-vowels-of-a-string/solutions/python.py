VOWELS = frozenset("aeiouAEIOU")


def solve(s: str) -> str:
    characters = list(s)
    left = 0
    right = len(characters) - 1

    while left < right:
        while left < right and characters[left] not in VOWELS:
            left += 1
        while left < right and characters[right] not in VOWELS:
            right -= 1
        if left < right:
            characters[left], characters[right] = characters[right], characters[left]
            left += 1
            right -= 1

    return "".join(characters)
