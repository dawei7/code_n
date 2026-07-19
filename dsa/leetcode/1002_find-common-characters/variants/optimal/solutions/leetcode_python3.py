from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for character in words[0]:
            common[ord(character) - ord("a")] += 1

        for word in words[1:]:
            current = [0] * 26
            for character in word:
                current[ord(character) - ord("a")] += 1
            for index in range(26):
                common[index] = min(common[index], current[index])

        answer = []
        for index, amount in enumerate(common):
            answer.extend([chr(ord("a") + index)] * amount)
        return answer
