class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rows = len(targetGrid)
        columns = len(targetGrid[0])
        colors = {color for row in targetGrid for color in row}
        bounds = {
            color: [rows, columns, -1, -1]
            for color in colors
        }

        for row in range(rows):
            for column in range(columns):
                color = targetGrid[row][column]
                box = bounds[color]
                box[0] = min(box[0], row)
                box[1] = min(box[1], column)
                box[2] = max(box[2], row)
                box[3] = max(box[3], column)

        graph = {color: set() for color in colors}
        indegree = {color: 0 for color in colors}
        for color, (top, left, bottom, right) in bounds.items():
            for row in range(top, bottom + 1):
                for column in range(left, right + 1):
                    covering = targetGrid[row][column]
                    if covering != color and covering not in graph[color]:
                        graph[color].add(covering)
                        indegree[covering] += 1

        ready = [color for color in colors if indegree[color] == 0]
        printed = 0
        while ready:
            color = ready.pop()
            printed += 1
            for covering in graph[color]:
                indegree[covering] -= 1
                if indegree[covering] == 0:
                    ready.append(covering)

        return printed == len(colors)
