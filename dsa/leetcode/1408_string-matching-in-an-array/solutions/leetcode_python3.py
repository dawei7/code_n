from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        for index, word in enumerate(words):
            if any(
                index != other_index and word in other
                for other_index, other in enumerate(words)
            ):
                matches.append(word)
        return matches
