from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for value in nums:
            if value != val:
                nums[write] = value
                write += 1
        return write
