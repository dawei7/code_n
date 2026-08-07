from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        value = nums[0]
        divided = value // k if value >= 0 else -((-value) // k)

        no_operation = value
        multiplying = value * k
        dividing = divided
        finished = -(10**30)
        answer = max(no_operation, multiplying, dividing)

        for value in nums[1:]:
            multiplied = value * k
            divided = value // k if value >= 0 else -((-value) // k)

            next_no_operation = max(value, no_operation + value)
            next_multiplying = max(
                multiplied,
                no_operation + multiplied,
                multiplying + multiplied,
            )
            next_dividing = max(
                divided,
                no_operation + divided,
                dividing + divided,
            )
            next_finished = max(
                multiplying + value,
                dividing + value,
                finished + value,
            )

            no_operation = next_no_operation
            multiplying = next_multiplying
            dividing = next_dividing
            finished = next_finished
            answer = max(
                answer,
                no_operation,
                multiplying,
                dividing,
                finished,
            )

        return answer
