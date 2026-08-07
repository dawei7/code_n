from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapped: list[str] = []

        for word in words:
            total = 0
            for character in word:
                total += weights[ord(character) - ord("a")]
            mapped.append(chr(ord("z") - total % 26))

        return "".join(mapped)
