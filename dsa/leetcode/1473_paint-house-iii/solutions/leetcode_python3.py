from typing import List


class Solution:
    def minCost(
        self,
        houses: List[int],
        cost: List[List[int]],
        m: int,
        n: int,
        target: int,
    ) -> int:
        infinity = 10**18

        previous = [[infinity] * n for _ in range(target + 1)]
        if houses[0] == 0:
            for color in range(n):
                previous[1][color] = cost[0][color]
        else:
            previous[1][houses[0] - 1] = 0

        for house_index in range(1, m):
            best = [(infinity, infinity, -1)] * (target + 1)

            for groups in range(1, min(target, house_index) + 1):
                smallest = infinity
                second_smallest = infinity
                smallest_color = -1

                for color, value in enumerate(previous[groups]):
                    if value < smallest:
                        second_smallest = smallest
                        smallest = value
                        smallest_color = color
                    elif value < second_smallest:
                        second_smallest = value

                best[groups] = (smallest, second_smallest, smallest_color)

            next_costs = [[infinity] * n for _ in range(target + 1)]
            if houses[house_index] == 0:
                available_colors = range(n)
            else:
                available_colors = (houses[house_index] - 1,)

            for groups in range(1, min(target, house_index + 1) + 1):
                for color in available_colors:
                    predecessor = previous[groups][color]

                    if groups > 1:
                        smallest, second_smallest, smallest_color = best[groups - 1]
                        different_color = (
                            smallest if smallest_color != color else second_smallest
                        )
                        predecessor = min(predecessor, different_color)

                    if predecessor == infinity:
                        continue

                    paint_cost = 0
                    if houses[house_index] == 0:
                        paint_cost = cost[house_index][color]
                    next_costs[groups][color] = predecessor + paint_cost

            previous = next_costs

        answer = min(previous[target])
        return -1 if answer == infinity else answer
