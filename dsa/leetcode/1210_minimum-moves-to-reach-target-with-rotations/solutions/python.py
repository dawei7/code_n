from collections import deque


def solve(grid):
    n = len(grid)
    start = (0, 0, 0)
    target = (n - 1, n - 2, 0)
    queue = deque([(0, 0, 0, 0)])
    seen = {start}

    while queue:
        r, c, orientation, steps = queue.popleft()
        if (r, c, orientation) == target:
            return steps

        if orientation == 0:
            if c + 2 < n and grid[r][c + 2] == 0:
                state = (r, c + 1, 0)
                if state not in seen:
                    seen.add(state)
                    queue.append((r, c + 1, 0, steps + 1))
            if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                for state in ((r + 1, c, 0), (r, c, 1)):
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, steps + 1))
        else:
            if r + 2 < n and grid[r + 2][c] == 0:
                state = (r + 1, c, 1)
                if state not in seen:
                    seen.add(state)
                    queue.append((r + 1, c, 1, steps + 1))
            if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                for state in ((r, c + 1, 1), (r, c, 0)):
                    if state not in seen:
                        seen.add(state)
                        queue.append((*state, steps + 1))

    return -1
