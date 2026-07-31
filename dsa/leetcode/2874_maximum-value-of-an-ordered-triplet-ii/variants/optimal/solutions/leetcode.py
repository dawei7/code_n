class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum_value = nums[0]
        maximum_difference = 0
        answer = 0

        for value in nums[1:]:
            answer = max(answer, maximum_difference * value)
            maximum_difference = max(
                maximum_difference,
                maximum_value - value,
            )
            maximum_value = max(maximum_value, value)

        return answer
