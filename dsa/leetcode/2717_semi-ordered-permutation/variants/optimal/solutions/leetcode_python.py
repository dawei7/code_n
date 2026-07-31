class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        one_index = nums.index(1)
        maximum_index = nums.index(len(nums))
        overlap = 1 if one_index > maximum_index else 0
        return one_index + len(nums) - 1 - maximum_index - overlap

