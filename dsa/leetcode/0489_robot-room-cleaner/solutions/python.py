"""Interface-preserving DFS backtracking for LeetCode 489."""


DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve(robot) -> None:
    visited: set[tuple[int, int]] = set()

    def go_back() -> None:
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(row: int, col: int, direction: int) -> None:
        visited.add((row, col))
        robot.clean()

        for offset in range(4):
            next_direction = (direction + offset) % 4
            delta_row, delta_col = DIRECTIONS[next_direction]
            next_cell = (row + delta_row, col + delta_col)
            if next_cell not in visited and robot.move():
                backtrack(next_cell[0], next_cell[1], next_direction)
                go_back()
            robot.turnRight()

    backtrack(0, 0, 0)
