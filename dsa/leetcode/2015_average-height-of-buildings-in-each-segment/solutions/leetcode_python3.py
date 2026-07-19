from collections import defaultdict
from typing import List


class Solution:
    def averageHeightOfBuildings(
        self, buildings: List[List[int]]
    ) -> List[List[int]]:
        changes = defaultdict(lambda: [0, 0])
        for start, end, height in buildings:
            changes[start][0] += height
            changes[start][1] += 1
            changes[end][0] -= height
            changes[end][1] -= 1

        answer = []
        total_height = 0
        active_count = 0
        previous = None

        for position in sorted(changes):
            if previous is not None and active_count:
                average = total_height // active_count
                if (
                    answer
                    and answer[-1][1] == previous
                    and answer[-1][2] == average
                ):
                    answer[-1][1] = position
                else:
                    answer.append([previous, position, average])

            height_change, count_change = changes[position]
            total_height += height_change
            active_count += count_change
            previous = position

        return answer
