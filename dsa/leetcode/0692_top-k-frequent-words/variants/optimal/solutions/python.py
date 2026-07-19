from collections import Counter
from heapq import heappush, heapreplace


def solve(words: list[str], k: int) -> list[str]:
    counts = Counter(words)
    heap = []

    for word, frequency in counts.items():
        reverse_word = tuple(-ord(character) for character in word) + (0,)
        candidate = (frequency, reverse_word, word)
        if len(heap) < k:
            heappush(heap, candidate)
        else:
            worst_frequency, _, worst_word = heap[0]
            if (
                frequency > worst_frequency
                or frequency == worst_frequency
                and word < worst_word
            ):
                heapreplace(heap, candidate)

    return sorted(
        (entry[2] for entry in heap),
        key=lambda word: (-counts[word], word),
    )

