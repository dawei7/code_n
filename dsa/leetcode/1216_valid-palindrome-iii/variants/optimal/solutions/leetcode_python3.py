class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        length = len(s)
        minimum_removals = [0] * length

        for left in range(length - 2, -1, -1):
            diagonal = 0
            for right in range(left + 1, length):
                previous_row = minimum_removals[right]
                if s[left] == s[right]:
                    minimum_removals[right] = diagonal
                else:
                    minimum_removals[right] = 1 + min(
                        minimum_removals[right], minimum_removals[right - 1]
                    )
                diagonal = previous_row

        return minimum_removals[-1] <= k
