class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        combined = word1 + word2
        boundary = len(word1)
        lengths = [0] * len(combined)
        answer = 0

        for left in range(len(combined) - 1, -1, -1):
            diagonal = 0
            lengths[left] = 1
            for right in range(left + 1, len(combined)):
                below = lengths[right]
                if combined[left] == combined[right]:
                    lengths[right] = diagonal + 2
                    if left < boundary <= right:
                        answer = max(answer, lengths[right])
                else:
                    lengths[right] = max(lengths[right], lengths[right - 1])
                diagonal = below

        return answer
