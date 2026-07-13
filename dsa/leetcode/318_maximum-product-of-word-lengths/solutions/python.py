def _maximum_product(words: list[str]) -> int:
    longest_by_mask: dict[int, int] = {}
    for word in words:
        mask = 0
        for letter in word:
            mask |= 1 << (ord(letter) - ord("a"))
        longest_by_mask[mask] = max(longest_by_mask.get(mask, 0), len(word))

    entries = list(longest_by_mask.items())
    best = 0
    for first in range(len(entries)):
        first_mask, first_length = entries[first]
        for second in range(first):
            second_mask, second_length = entries[second]
            if first_mask & second_mask == 0:
                best = max(best, first_length * second_length)
    return best


def solve(words: list[str]) -> int:
    return _maximum_product(words)
