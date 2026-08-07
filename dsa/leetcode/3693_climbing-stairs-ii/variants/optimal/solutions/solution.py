from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        one_step_back = 0
        two_steps_back = float("inf")
        three_steps_back = float("inf")

        for step in range(1, n + 1):
            best = costs[step - 1] + min(
                one_step_back + 1,
                two_steps_back + 4,
                three_steps_back + 9,
            )
            three_steps_back, two_steps_back, one_step_back = (
                two_steps_back,
                one_step_back,
                best,
            )

        return one_step_back
