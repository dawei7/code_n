from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drops = 0
        pivot = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                pivot = i
        if drops == 0:
            return 0
        if drops == 1:
            return (n - 1 - pivot) % n
        return -1
