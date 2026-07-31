class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        answer = 1
        ending_here = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                ending_here += 1
            else:
                ending_here = 1
            answer += ending_here

        return answer
