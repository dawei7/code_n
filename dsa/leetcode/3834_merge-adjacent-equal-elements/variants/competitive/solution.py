class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        merged = []

        for number in nums:
            while merged and merged[-1] == number:
                merged.pop()
                number *= 2
            merged.append(number)

        return merged
