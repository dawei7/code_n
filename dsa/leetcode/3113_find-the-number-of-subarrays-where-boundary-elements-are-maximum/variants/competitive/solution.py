class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        answer = 0

        for value in nums:
            while stack and stack[-1][0] < value:
                stack.pop()

            if stack and stack[-1][0] == value:
                stack[-1][1] += 1
            else:
                stack.append([value, 1])

            answer += stack[-1][1]

        return answer
