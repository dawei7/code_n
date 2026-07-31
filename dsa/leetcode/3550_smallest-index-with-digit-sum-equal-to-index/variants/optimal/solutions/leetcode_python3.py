class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, value in enumerate(nums[:28]):
            if sum(map(int, str(value))) == index:
                return index
        return -1
