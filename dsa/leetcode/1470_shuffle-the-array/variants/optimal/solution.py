class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        for index in range(n):
            shuffled.append(nums[index])
            shuffled.append(nums[index + n])
        return shuffled
