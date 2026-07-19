class Solution:
    def binaryGap(self, n: int) -> int:
        previous_one = -1
        position = 0
        longest_gap = 0

        while n:
            if n & 1:
                if previous_one >= 0:
                    longest_gap = max(longest_gap, position - previous_one)
                previous_one = position
            position += 1
            n >>= 1

        return longest_gap
