from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        depth = 0
        for character in seq:
            if character == "(":
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1
        return answer
