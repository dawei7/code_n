from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        answer = [words[0]]
        last_group = groups[0]

        for word, group in zip(words[1:], groups[1:]):
            if group != last_group:
                answer.append(word)
                last_group = group

        return answer
