from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [
            words[index + 2]
            for index in range(len(words) - 2)
            if words[index] == first and words[index + 1] == second
        ]
