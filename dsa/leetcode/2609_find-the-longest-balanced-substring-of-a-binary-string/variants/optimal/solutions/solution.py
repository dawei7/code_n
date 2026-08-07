class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longest = 0
        zeroes = 0
        ones = 0

        for character in s:
            if character == "0":
                if ones > 0:
                    zeroes = 0
                    ones = 0
                zeroes += 1
            else:
                ones += 1
                longest = max(longest, 2 * min(zeroes, ones))

        return longest
