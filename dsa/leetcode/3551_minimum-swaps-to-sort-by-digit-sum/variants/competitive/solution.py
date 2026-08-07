class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        key = lambda x: (sum(map(int, str(x))), x)
        target = sorted(nums, key=key)
        position = {x: i for i, x in enumerate(nums)}
        swaps = 0
        for i, x in enumerate(target):
            j = position[x]
            if i != j:
                y = nums[i]
                nums[i], nums[j] = nums[j], y
                position[x], position[y] = i, j
                swaps += 1
        return swaps
