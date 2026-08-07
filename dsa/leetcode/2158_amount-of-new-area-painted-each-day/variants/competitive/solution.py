from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        next_unpainted = {}

        def find(position):
            path = []
            while position in next_unpainted:
                path.append(position)
                position = next_unpainted[position]
            for skipped in path:
                next_unpainted[skipped] = position
            return position

        worklog = []
        for start, end in paint:
            after_interval = find(end)
            position = find(start)
            fresh_area = 0

            while position < end:
                next_position = find(position + 1)
                next_unpainted[position] = after_interval
                fresh_area += 1
                position = next_position

            worklog.append(fresh_area)

        return worklog
