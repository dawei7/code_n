from collections import deque
from typing import List


class Solution:
    def maximumRobots(
        self,
        chargeTimes: List[int],
        runningCosts: List[int],
        budget: int,
    ) -> int:
        maximum_charge_indices = deque()
        running_sum = 0
        left = 0
        best = 0

        for right, charge_time in enumerate(chargeTimes):
            running_sum += runningCosts[right]
            while (
                maximum_charge_indices
                and chargeTimes[maximum_charge_indices[-1]] <= charge_time
            ):
                maximum_charge_indices.pop()
            maximum_charge_indices.append(right)

            while (
                maximum_charge_indices
                and chargeTimes[maximum_charge_indices[0]]
                + (right - left + 1) * running_sum
                > budget
            ):
                if maximum_charge_indices[0] == left:
                    maximum_charge_indices.popleft()
                running_sum -= runningCosts[left]
                left += 1

            best = max(best, right - left + 1)

        return best
