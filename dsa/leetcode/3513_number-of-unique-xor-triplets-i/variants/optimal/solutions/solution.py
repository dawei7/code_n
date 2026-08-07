class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return size
        return 1 << size.bit_length()
