from collections import defaultdict


def solve(phrases: list[str]) -> list[str]:
    last_words = []
    suffixes = []
    by_first = defaultdict(list)

    for index, phrase in enumerate(phrases):
        words = phrase.split()
        last_words.append(words[-1])
        suffixes.append(phrase[len(words[0]):])
        by_first[words[0]].append(index)

    merged = set()
    for before, last_word in enumerate(last_words):
        for after in by_first.get(last_word, ()):
            if before != after:
                merged.add(phrases[before] + suffixes[after])

    return sorted(merged)
