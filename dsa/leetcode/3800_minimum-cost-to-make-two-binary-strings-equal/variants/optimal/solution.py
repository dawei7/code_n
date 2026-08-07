class Solution:
    def minimumCost(
        self,
        s: str,
        t: str,
        flipCost: int,
        swapCost: int,
        crossCost: int,
    ) -> int:
        zero_to_one = 0
        one_to_zero = 0

        for source, target in zip(s, t):
            if source == target:
                continue
            if source == "0":
                zero_to_one += 1
            else:
                one_to_zero += 1

        opposite_pairs = min(zero_to_one, one_to_zero)
        remainder = abs(zero_to_one - one_to_zero)
        opposite_cost = min(swapCost, 2 * flipCost)
        same_cost = min(crossCost + swapCost, 2 * flipCost)

        return opposite_pairs * opposite_cost + (remainder // 2) * same_cost + (remainder % 2) * flipCost
