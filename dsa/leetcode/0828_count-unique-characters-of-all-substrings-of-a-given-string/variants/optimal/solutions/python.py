ALPHABET_SIZE = 26


def solve(s: str) -> int:
    previous = [-1] * ALPHABET_SIZE
    before_previous = [-1] * ALPHABET_SIZE
    total = 0

    for index, character in enumerate(s):
        letter = ord(character) - ord("A")
        last = previous[letter]
        total += (last - before_previous[letter]) * (index - last)
        before_previous[letter] = last
        previous[letter] = index

    length = len(s)
    for letter in range(ALPHABET_SIZE):
        last = previous[letter]
        total += (last - before_previous[letter]) * (length - last)

    return total
