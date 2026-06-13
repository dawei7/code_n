"""Optimal solution for graph_18: A* Search on a 2D grid.

Manhattan-distance heuristic. Walk the grid with 4-neighbour
moves; a priority queue keyed on f = g + h (cost so far plus
Manhattan distance to goal) drives the expansion order.
Return the shortest path length in steps, or -1 if no path.
"""


def solve(grid, start, goal, size):
    from heapq import heappush, heappop
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    if start == goal:
        return 0

    def heuristic(p):
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

    open_heap = []
    heappush(open_heap, (heuristic(start), 0, start))
    g_score = {start: 0}
    while open_heap:
        f, g, current = heappop(open_heap)
        if current == goal:
            return g
        if g > g_score.get(current, float("inf")):
            continue
        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                nbr = (nr, nc)
                tentative = g + 1
                if tentative < g_score.get(nbr, float("inf")):
                    g_score[nbr] = tentative
                    heappush(open_heap, (tentative + heuristic(nbr), tentative, nbr))
    return -1
