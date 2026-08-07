class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        negative_infinity = float("-inf")
        previous = [negative_infinity] * (len(nums2) + 1)

        for left in nums1:
            current = [negative_infinity] * (len(nums2) + 1)
            for column, right in enumerate(nums2, 1):
                product = left * right
                pair = product + max(0, previous[column - 1])
                current[column] = max(
                    pair,
                    previous[column],
                    current[column - 1],
                )
            previous = current

        return previous[-1]
