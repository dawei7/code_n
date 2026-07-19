from collections import Counter


def solve(words: list[str]) -> bool:
    word_count = len(words)
    frequencies = Counter(character for word in words for character in word)
    return all(count % word_count == 0 for count in frequencies.values())
