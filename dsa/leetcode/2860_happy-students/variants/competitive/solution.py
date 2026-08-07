class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = int(nums[0] > 0)

        for selected in range(1, n):
            if nums[selected - 1] < selected < nums[selected]:
                answer += 1

        if nums[-1] < n:
            answer += 1

        return answer
