


def solve():
    class Solution:
        def atMostK(self, nums, k):
            count = defaultdict(int)
            left = res = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res

        def subarraysWithKDistinct(self, nums, k):
            return self.atMostK(nums, k) - self.atMostK(nums, k - 1)


if __name__ == "__main__":
    solve()
