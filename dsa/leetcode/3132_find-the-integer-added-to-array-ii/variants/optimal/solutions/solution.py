class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        for start in range(2, -1, -1):
            x = nums2[0] - nums1[start]
            j = 0
            for value in nums1:
                if j < len(nums2) and value + x == nums2[j]:
                    j += 1
            if j == len(nums2):
                return x
