from collections import deque
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robots = sorted(robot)
        factories = sorted(factory)
        robot_count = len(robots)
        infinity = 10**30
        previous = [0] + [infinity] * robot_count

        for position, capacity in factories:
            prefix = [0] * (robot_count + 1)
            for count, robot_position in enumerate(robots, 1):
                prefix[count] = prefix[count - 1] + abs(robot_position - position)

            current = [infinity] * (robot_count + 1)
            choices = deque()

            for count in range(robot_count + 1):
                value = previous[count] - prefix[count]
                while choices and (previous[choices[-1]] - prefix[choices[-1]] >= value):
                    choices.pop()
                choices.append(count)

                while choices[0] < count - capacity:
                    choices.popleft()

                start = choices[0]
                current[count] = prefix[count] + previous[start] - prefix[start]

            previous = current

        return previous[robot_count]
