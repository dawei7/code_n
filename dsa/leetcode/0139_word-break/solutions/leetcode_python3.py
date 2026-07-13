from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        reachable = [False] * (len(s) + 1)
        reachable[0] = True
        for end in range(1, len(s) + 1):
            for start in range(end):
                if reachable[start] and s[start:end] in words:
                    reachable[end] = True
                    break
        return reachable[-1]
