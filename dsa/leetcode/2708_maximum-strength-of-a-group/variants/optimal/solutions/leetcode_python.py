class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        maximum = nums[0]
        minimum = nums[0]

        for value in nums[1:]:
            previous_maximum = maximum
            previous_minimum = minimum
            maximum = max(
                previous_maximum,
                value,
                previous_maximum * value,
                previous_minimum * value,
            )
            minimum = min(
                previous_minimum,
                value,
                previous_maximum * value,
                previous_minimum * value,
            )

        return maximum
