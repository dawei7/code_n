from bisect import bisect_left


class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = sorted(zip(costs, capacity))
        sorted_costs = [cost for cost, _ in machines]

        prefix_best = []
        best_capacity = 0
        for _, machine_capacity in machines:
            best_capacity = max(best_capacity, machine_capacity)
            prefix_best.append(best_capacity)

        answer = 0
        for index, (cost, machine_capacity) in enumerate(machines):
            if cost < budget:
                answer = max(answer, machine_capacity)

            partner_count = bisect_left(
                sorted_costs,
                budget - cost,
                0,
                index,
            )
            if partner_count:
                answer = max(
                    answer,
                    machine_capacity + prefix_best[partner_count - 1],
                )

        return answer
