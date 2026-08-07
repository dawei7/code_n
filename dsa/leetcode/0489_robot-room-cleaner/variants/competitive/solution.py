# LeetCode supplies this interface; the solution must not inspect its implementation.
# class Robot:
#     def move(self) -> bool: ...
#     def turnLeft(self) -> None: ...
#     def turnRight(self) -> None: ...
#     def clean(self) -> None: ...


class Solution:
    def cleanRoom(self, robot):
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(row, col, direction):
            visited.add((row, col))
            robot.clean()

            for offset in range(4):
                next_direction = (direction + offset) % 4
                delta_row, delta_col = directions[next_direction]
                next_cell = (row + delta_row, col + delta_col)
                if next_cell not in visited and robot.move():
                    backtrack(next_cell[0], next_cell[1], next_direction)
                    go_back()
                robot.turnRight()

        backtrack(0, 0, 0)
