from typing import List


class Solution:
    def sumEvenAfterQueries(
        self,
        nums: List[int],
        queries: List[List[int]],
    ) -> List[int]:
        even_sum = sum(value for value in nums if value % 2 == 0)
        answer = []

        for value, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            answer.append(even_sum)

        return answer
