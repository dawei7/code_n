from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sift_down(root: int, end: int) -> None:
            while 2 * root + 1 <= end:
                child = 2 * root + 1
                if child + 1 <= end and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] >= nums[child]:
                    return
                nums[root], nums[child] = nums[child], nums[root]
                root = child

        for root in range(len(nums) // 2 - 1, -1, -1):
            sift_down(root, len(nums) - 1)

        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end - 1)

        return nums
