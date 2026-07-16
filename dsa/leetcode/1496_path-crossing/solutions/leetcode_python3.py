class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = {(0, 0)}

        for move in path:
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            else:
                x -= 1

            position = (x, y)
            if position in visited:
                return True
            visited.add(position)

        return False
