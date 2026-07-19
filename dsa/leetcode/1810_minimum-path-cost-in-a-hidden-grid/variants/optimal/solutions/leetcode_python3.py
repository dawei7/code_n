from heapq import heappop, heappush


class Solution:
    def findShortestPath(self, master: "GridMaster") -> int:
        directions = (
            ("U", -1, 0, "D"),
            ("R", 0, 1, "L"),
            ("D", 1, 0, "U"),
            ("L", 0, -1, "R"),
        )
        costs = {(0, 0): 0}
        target = None
        stack = [[0, 0, 0, None]]

        while stack:
            row, column, next_direction, back_direction = stack[-1]
            if next_direction == len(directions):
                stack.pop()
                if back_direction is not None:
                    master.move(back_direction)
                continue

            direction, row_delta, column_delta, opposite = directions[next_direction]
            stack[-1][2] += 1
            neighbor = (row + row_delta, column + column_delta)
            if neighbor in costs or not master.canMove(direction):
                continue

            costs[neighbor] = master.move(direction)
            if master.isTarget():
                target = neighbor
            stack.append([neighbor[0], neighbor[1], 0, opposite])

        if target is None:
            return -1

        distances = {(0, 0): 0}
        heap = [(0, 0, 0)]
        while heap:
            distance, row, column = heappop(heap)
            position = (row, column)
            if distance != distances[position]:
                continue
            if position == target:
                return distance

            for _, row_delta, column_delta, _ in directions:
                neighbor = (row + row_delta, column + column_delta)
                if neighbor not in costs:
                    continue
                candidate = distance + costs[neighbor]
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor[0], neighbor[1]))

        return -1
