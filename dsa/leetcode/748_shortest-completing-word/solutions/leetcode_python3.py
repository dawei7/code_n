from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = [0] * 26
        for character in licensePlate.lower():
            if "a" <= character <= "z":
                required[ord(character) - ord("a")] += 1

        best = ""
        for word in words:
            counts = [0] * 26
            for character in word:
                counts[ord(character) - ord("a")] += 1

            if (
                all(counts[index] >= required[index] for index in range(26))
                and (not best or len(word) < len(best))
            ):
                best = word

        return best
