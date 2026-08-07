class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        best_range = -1
        answer = 0

        for value in nums:
            remaining = value
            smallest = 9
            largest = 0

            while remaining:
                digit = remaining % 10
                smallest = min(smallest, digit)
                largest = max(largest, digit)
                remaining //= 10

            digit_range = largest - smallest
            if digit_range > best_range:
                best_range = digit_range
                answer = value
            elif digit_range == best_range:
                answer += value

        return answer
