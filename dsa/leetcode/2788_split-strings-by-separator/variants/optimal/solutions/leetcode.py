from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            for part in word.split(separator):
                if part:
                    result.append(part)

        return result
