class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maximum = 0
        score = 0
        answer = []

        for value in nums:
            maximum = max(maximum, value)
            score += value + maximum
            answer.append(score)

        return answer
