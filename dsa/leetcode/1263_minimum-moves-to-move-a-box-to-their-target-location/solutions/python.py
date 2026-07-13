from collections import deque


def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    box = player = target = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "B":
                box = (r, c)
            elif grid[r][c] == "S":
                player = (r, c)
            elif grid[r][c] == "T":
                target = (r, c)

    def free(cell, blocked_box):
        r, c = cell
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and cell != blocked_box

    def can_reach(start, goal, blocked_box):
        queue = deque([start])
        seen = {start}
        while queue:
            cell = queue.popleft()
            if cell == goal:
                return True
            r, c = cell
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt = (r + dr, c + dc)
                if nxt not in seen and free(nxt, blocked_box):
                    seen.add(nxt)
                    queue.append(nxt)
        return False

    queue = deque([(box, player, 0)])
    seen = {(box, player)}
    while queue:
        current_box, current_player, pushes = queue.popleft()
        if current_box == target:
            return pushes
        br, bc = current_box
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            stand = (br - dr, bc - dc)
            next_box = (br + dr, bc + dc)
            if not free(next_box, current_box) or not free(stand, current_box):
                continue
            if not can_reach(current_player, stand, current_box):
                continue
            state = (next_box, current_box)
            if state not in seen:
                seen.add(state)
                queue.append((next_box, current_box, pushes + 1))
    return -1
