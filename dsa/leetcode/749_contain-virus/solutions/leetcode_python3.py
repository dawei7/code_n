from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows = len(isInfected)
        columns = len(isInfected[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        walls_built = 0

        while True:
            seen = set()
            regions = []
            frontiers = []
            wall_counts = []

            for row in range(rows):
                for column in range(columns):
                    if isInfected[row][column] != 1 or (row, column) in seen:
                        continue

                    region = []
                    frontier = set()
                    wall_count = 0
                    stack = [(row, column)]
                    seen.add((row, column))

                    while stack:
                        current_row, current_column = stack.pop()
                        region.append((current_row, current_column))
                        for row_delta, column_delta in directions:
                            next_row = current_row + row_delta
                            next_column = current_column + column_delta
                            if not (0 <= next_row < rows and 0 <= next_column < columns):
                                continue
                            if isInfected[next_row][next_column] == 0:
                                frontier.add((next_row, next_column))
                                wall_count += 1
                            elif (
                                isInfected[next_row][next_column] == 1
                                and (next_row, next_column) not in seen
                            ):
                                seen.add((next_row, next_column))
                                stack.append((next_row, next_column))

                    regions.append(region)
                    frontiers.append(frontier)
                    wall_counts.append(wall_count)

            if not regions:
                break

            quarantine = max(range(len(regions)), key=lambda index: len(frontiers[index]))
            if not frontiers[quarantine]:
                break

            walls_built += wall_counts[quarantine]
            for row, column in regions[quarantine]:
                isInfected[row][column] = -1

            for index, frontier in enumerate(frontiers):
                if index == quarantine:
                    continue
                for row, column in frontier:
                    isInfected[row][column] = 1

        return walls_built
