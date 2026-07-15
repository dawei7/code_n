from collections import Counter
from typing import List


class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:
        def matches(first: str, second: str) -> int:
            return sum(left == right for left, right in zip(first, second))

        candidates = list(words)
        while candidates:
            guess = min(
                candidates,
                key=lambda word: max(
                    Counter(matches(word, candidate) for candidate in candidates).values()
                ),
            )
            score = master.guess(guess)
            if score == 6:
                return
            candidates = [
                candidate for candidate in candidates if matches(guess, candidate) == score
            ]
