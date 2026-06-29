


def solve():
    class Solution:
        def count_non_minimum(self, nums):
            if not nums:
                return 0

            minimum = min(nums)
            count_min = nums.count(minimum)

            return len(nums) - count_min


if __name__ == "__main__":
    solve()
