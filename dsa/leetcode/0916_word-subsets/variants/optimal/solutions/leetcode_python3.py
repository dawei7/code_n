from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = [0] * 26

        for word in words2:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord("a")] += 1
            for index in range(26):
                required[index] = max(required[index], counts[index])

        universal = []
        for word in words1:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord("a")] += 1
            if all(counts[index] >= required[index] for index in range(26)):
                universal.append(word)

        return universal

