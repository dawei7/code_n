class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        deficit = [0] * 26
        for character in word2:
            deficit[ord(character) - ord("a")] += 1

        missing = len(word2)
        left = 0
        answer = 0

        for character in word1:
            index = ord(character) - ord("a")
            if deficit[index] > 0:
                missing -= 1
            deficit[index] -= 1

            while missing == 0:
                left_index = ord(word1[left]) - ord("a")
                deficit[left_index] += 1
                left += 1
                if deficit[left_index] > 0:
                    missing += 1

            answer += left

        return answer
