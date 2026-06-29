


def solve():
    class Solution:
        def missingNumber(self, nums):
            n = len(nums)
            sum1 = sum(nums)        # Sum of array elements
            sum2 = n * (n + 1) // 2 # Sum of numbers from 0 to n
            return abs(sum2 - sum1)


if __name__ == "__main__":
    solve()
