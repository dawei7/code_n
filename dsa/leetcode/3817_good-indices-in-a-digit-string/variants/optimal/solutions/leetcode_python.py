from typing import List


class Solution:
    def goodIndices(self, s: str) -> List[int]:
        answer = []

        for index in range(len(s)):
            representation = str(index)
            start = index - len(representation) + 1
            if start >= 0 and s[start : index + 1] == representation:
                answer.append(index)

        return answer
