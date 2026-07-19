from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        unreachable = -(target + 1)
        maximum_digits = [unreachable] * (target + 1)
        maximum_digits[0] = 0

        for total in range(1, target + 1):
            for price in cost:
                if total >= price:
                    maximum_digits[total] = max(
                        maximum_digits[total],
                        maximum_digits[total - price] + 1,
                    )

        if maximum_digits[target] < 0:
            return "0"

        answer = []
        remaining = target
        for digit in range(9, 0, -1):
            price = cost[digit - 1]
            while (
                remaining >= price
                and maximum_digits[remaining]
                == maximum_digits[remaining - price] + 1
            ):
                answer.append(str(digit))
                remaining -= price

        return "".join(answer)
