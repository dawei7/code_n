from heapq import heappop, heappush


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        prefix_sum = 0
        operations = 0
        negatives = []

        for number in nums:
            prefix_sum += number
            if number < 0:
                heappush(negatives, number)

            if prefix_sum < 0:
                prefix_sum -= heappop(negatives)
                operations += 1

        return operations
