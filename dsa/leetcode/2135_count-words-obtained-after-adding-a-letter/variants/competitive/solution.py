from typing import List


class Solution:
    def wordCount(
        self,
        startWords: List[str],
        targetWords: List[str],
    ) -> int:
        def mask(word: str) -> int:
            value = 0
            for letter in word:
                value |= 1 << (ord(letter) - ord("a"))
            return value

        starts = {mask(word) for word in startWords}
        answer = 0
        for word in targetWords:
            target = mask(word)
            if any((target ^ (1 << (ord(letter) - ord("a")))) in starts for letter in word):
                answer += 1
        return answer
