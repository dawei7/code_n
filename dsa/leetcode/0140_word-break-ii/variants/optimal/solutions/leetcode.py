from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @cache
        def sentences(start):
            if start == len(s):
                return ("",)
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for suffix in sentences(end):
                        result.append(word if not suffix else word + " " + suffix)
            return tuple(result)

        return list(sentences(0))
