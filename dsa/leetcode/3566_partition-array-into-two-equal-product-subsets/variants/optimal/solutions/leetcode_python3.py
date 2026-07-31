from math import prod


class Solution:
    def checkEqualPartitions(self, nums: list[int], target: int) -> bool:
        if prod(nums) != target * target:
            return False
        length = len(nums)

        def search(index: int, product: int, selected: bool) -> bool:
            if product == target:
                return selected
            if index == length or product > target or target % product != 0:
                return False
            return search(index + 1, product * nums[index], True) or search(index + 1, product, selected)

        return search(0, 1, False)
