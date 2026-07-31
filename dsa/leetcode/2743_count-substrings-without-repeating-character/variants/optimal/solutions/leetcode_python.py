class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        last_seen = [-1] * 26
        left = 0
        answer = 0

        for right, character in enumerate(s):
            index = ord(character) - ord('a')
            left = max(left, last_seen[index] + 1)
            last_seen[index] = right
            answer += right - left + 1

        return answer
