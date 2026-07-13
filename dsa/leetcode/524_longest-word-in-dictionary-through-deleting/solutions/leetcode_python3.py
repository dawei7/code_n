from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str) -> bool:
            index = 0
            for character in s:
                if index < len(word) and word[index] == character:
                    index += 1
            return index == len(word)

        answer = ""
        for word in dictionary:
            if is_subsequence(word) and (
                len(word) > len(answer) or (len(word) == len(answer) and word < answer)
            ):
                answer = word
        return answer
