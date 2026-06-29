


def solve():
    class Solution(object):
        def check(self, nums):
            drops = 0
            n = len(nums)
            for i in range(n):
                if nums[i] > nums[(i + 1) % n]:
                    drops += 1
            return drops <= 1


if __name__ == "__main__":
    solve()
