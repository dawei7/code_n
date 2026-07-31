from collections import deque


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        prefix_nums = sum(nums)
        prefix_cost = sum(cost)
        total_cost = prefix_cost
        lines = deque()

        def add_line(slope: int, intercept: int) -> None:
            line = (slope, intercept)
            while len(lines) >= 2:
                m1, b1 = lines[-2]
                m2, b2 = lines[-1]
                if (b1 - b2) * (slope - m2) <= (b2 - intercept) * (m2 - m1):
                    lines.pop()
                else:
                    break
            lines.append(line)

        def value(line: tuple[int, int], x: int) -> int:
            return line[0] * x + line[1]

        add_line(
            -(prefix_nums + k),
            prefix_nums * prefix_cost + k * total_cost,
        )
        answer = 0

        for index in range(len(nums) - 1, -1, -1):
            prefix_nums -= nums[index]
            prefix_cost -= cost[index]
            while len(lines) >= 2 and value(lines[0], prefix_cost) >= value(lines[1], prefix_cost):
                lines.popleft()
            answer = value(lines[0], prefix_cost)
            add_line(
                -(prefix_nums + k),
                answer + prefix_nums * prefix_cost + k * total_cost,
            )

        return answer
