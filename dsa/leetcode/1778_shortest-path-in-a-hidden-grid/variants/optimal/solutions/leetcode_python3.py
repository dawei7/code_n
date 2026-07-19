from collections import deque


class Solution:
    def findShortestPath(self, master: "GridMaster") -> int:
        directions = (
            ("U", -1, 0, "D"),
            ("R", 0, 1, "L"),
            ("D", 1, 0, "U"),
            ("L", 0, -1, "R"),
        )
        reachable = {(0, 0)}
        target = (0, 0) if master.isTarget() else None
        stack = [[0, 0, 0, None]]

        while stack:
            row, column, next_direction, back_direction = stack[-1]
            if next_direction == len(directions):
                stack.pop()
                if back_direction is not None:
                    master.move(back_direction)
                continue

            direction, row_delta, column_delta, opposite = directions[
                next_direction
            ]
            stack[-1][2] += 1
            neighbor = (row + row_delta, column + column_delta)
            if neighbor in reachable or not master.canMove(direction):
                continue

            master.move(direction)
            reachable.add(neighbor)
            if master.isTarget():
                target = neighbor
            stack.append([neighbor[0], neighbor[1], 0, opposite])

        if target is None:
            return -1

        queue = deque([((0, 0), 0)])
        seen = {(0, 0)}
        while queue:
            (row, column), distance = queue.popleft()
            if (row, column) == target:
                return distance
            for _, row_delta, column_delta, _ in directions:
                neighbor = (row + row_delta, column + column_delta)
                if neighbor in reachable and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return -1
