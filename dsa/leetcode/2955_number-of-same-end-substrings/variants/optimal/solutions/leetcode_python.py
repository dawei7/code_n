from typing import List


class Solution:
    def sameEndSubstringCount(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        prefix = [[0] * 26]

        for character in s:
            current = prefix[-1].copy()
            current[ord(character) - ord("a")] += 1
            prefix.append(current)

        answer = []
        for left, right in queries:
            total = 0
            for letter in range(26):
                frequency = prefix[right + 1][letter] - prefix[left][letter]
                total += frequency * (frequency + 1) // 2
            answer.append(total)

        return answer
