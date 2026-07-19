from typing import List


class Solution:
    def closestCost(
        self,
        baseCosts: List[int],
        toppingCosts: List[int],
        target: int,
    ) -> int:
        topping_sums = {0}
        for cost in toppingCosts:
            topping_sums |= {
                current + copies * cost
                for current in tuple(topping_sums)
                for copies in (1, 2)
            }

        answer = baseCosts[0]
        for base in baseCosts:
            for topping_sum in topping_sums:
                total = base + topping_sum
                if (abs(total - target), total) < (
                    abs(answer - target),
                    answer,
                ):
                    answer = total
        return answer
