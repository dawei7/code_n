from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        answer = 0
        last_index = len(words) - 1

        for index, word in enumerate(words):
            if word != words[0]:
                answer = max(answer, index + 1)
            if word != words[last_index]:
                answer = max(answer, last_index - index + 1)

        return answer
