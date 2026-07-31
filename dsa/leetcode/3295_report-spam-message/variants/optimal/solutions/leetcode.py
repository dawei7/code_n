from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        matches = 0
        for word in message:
            if word in banned:
                matches += 1
                if matches == 2:
                    return True
        return False
