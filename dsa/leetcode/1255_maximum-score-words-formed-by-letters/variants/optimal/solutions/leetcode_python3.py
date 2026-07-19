from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)
        word_counts = [Counter(word) for word in words]
        word_scores = [sum(score[ord(char) - ord("a")] * count for char, count in counts.items()) for counts in word_counts]

        def search(index: int, remaining: Counter) -> int:
            if index == len(words):
                return 0
            best = search(index + 1, remaining)
            counts = word_counts[index]
            if all(remaining[char] >= count for char, count in counts.items()):
                next_remaining = remaining.copy()
                for char, count in counts.items():
                    next_remaining[char] -= count
                best = max(best, word_scores[index] + search(index + 1, next_remaining))
            return best

        return search(0, available)
