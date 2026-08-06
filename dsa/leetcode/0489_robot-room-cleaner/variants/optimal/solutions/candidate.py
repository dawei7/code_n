"""Iterative coordinate DFS for LeetCode 489."""


def solve(robot) -> None:
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = {(0, 0)}

    def go_back() -> None:
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    robot.clean()
    stack = [[0, 0, 0, 0]]

    while stack:
        row, col, direction, offset = stack[-1]
        if offset == 4:
            stack.pop()
            if stack:
                go_back()
                robot.turnRight()
                stack[-1][3] += 1
            continue

        next_direction = (direction + offset) % 4
        delta_row, delta_col = directions[next_direction]
        next_cell = (row + delta_row, col + delta_col)

        if next_cell not in visited and robot.move():
            visited.add(next_cell)
            robot.clean()
            stack.append([next_cell[0], next_cell[1], next_direction, 0])
            continue

        robot.turnRight()
        stack[-1][3] += 1
