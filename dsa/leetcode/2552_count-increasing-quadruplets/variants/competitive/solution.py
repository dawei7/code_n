class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        triplets = [0] * len(nums)
        answer = 0

        for fourth in range(len(nums)):
            smaller = 0

            for middle in range(fourth):
                if nums[middle] < nums[fourth]:
                    answer += triplets[middle]
                    smaller += 1
                else:
                    triplets[middle] += smaller

        return answer
