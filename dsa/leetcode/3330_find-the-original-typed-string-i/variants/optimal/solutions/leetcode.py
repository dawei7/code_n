class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1

        for index in range(1, len(word)):
            if word[index] == word[index - 1]:
                answer += 1

        return answer
