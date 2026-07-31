class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        answer = 0
        number = 0
        weight = 1

        for character in s[::-1]:
            if character == "0":
                answer += 1
                weight *= 2
            elif number + weight <= k:
                number += weight
                answer += 1
                weight *= 2

        return answer
