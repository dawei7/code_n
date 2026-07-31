class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97,
        }

        first = next(
            index for index, value in enumerate(nums) if value in primes
        )
        last = next(
            index
            for index in range(len(nums) - 1, -1, -1)
            if nums[index] in primes
        )
        return last - first
