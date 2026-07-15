from collections import Counter
from typing import List


def solve(words: List[str], letters: List[str], score: List[int]) -> int:
    available = Counter(letters)
    word_counts = [Counter(word) for word in words]
    word_scores = [sum(score[ord(ch) - ord("a")] * count for ch, count in counts.items()) for counts in word_counts]

    def backtrack(index, remaining):
        if index == len(words):
            return 0
        best = backtrack(index + 1, remaining)
        counts = word_counts[index]
        if all(remaining[ch] >= count for ch, count in counts.items()):
            next_remaining = remaining.copy()
            for ch, count in counts.items():
                next_remaining[ch] -= count
            best = max(best, word_scores[index] + backtrack(index + 1, next_remaining))
        return best

    return backtrack(0, available)
