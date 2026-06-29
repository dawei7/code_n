


def solve():
    class Solution:
        def singleNumber(self, nums):
            result = 0
            for num in nums:
                result ^= num  # XOR accumulates the unique number
            return result


if __name__ == "__main__":
    solve()
