from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_by_value = {value: index for index, value in enumerate(nums2)}
        return [index_by_value[value] for value in nums1]
