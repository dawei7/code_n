from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        return all(word[0] == character for word, character in zip(words, s))
