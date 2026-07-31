class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = total_sum
        right_product = 1
        overflow_value = total_sum + 1
        answer = -1

        for index in range(len(nums) - 1, -1, -1):
            left_sum -= nums[index]
            if left_sum == right_product:
                answer = index

            if right_product > total_sum // nums[index]:
                right_product = overflow_value
            else:
                right_product *= nums[index]

        return answer
