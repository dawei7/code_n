from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_letters = set(allowed)
        return sum(
            all(character in allowed_letters for character in word)
            for word in words
        )
