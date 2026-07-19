"""Optimal app-local solution for LeetCode 874."""


def solve(commands, obstacles):
    blocked = {tuple(obstacle) for obstacle in obstacles}
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = 0
    x = 0
    y = 0
    best = 0

    for command in commands:
        if command == -2:
            direction = (direction - 1) % 4
        elif command == -1:
            direction = (direction + 1) % 4
        else:
            dx, dy = directions[direction]
            for _ in range(command):
                next_x = x + dx
                next_y = y + dy
                if (next_x, next_y) in blocked:
                    break
                x = next_x
                y = next_y
                best = max(best, x * x + y * y)

    return best
