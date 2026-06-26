"""Optimal solution for bb_04: 8-Puzzle (Branch and Bound).

Solve the 8-puzzle (3x3 sliding-tile puzzle with
"""


def solve(start, goal):
    """8-puzzle via B&B with misplaced-tiles heuristic.

    Return the minimum number of moves (depth) of the goal
    node, or -1 if no solution is found within the search
    budget.
    """
    import heapq
    N = 3
    # Flatten the goal to a tuple for O(1) hashing.
    goal_flat = tuple(sum(goal, []))

    def misplaced(board_flat):
        return sum(1 for i, v in enumerate(board_flat) if v != 0 and v != goal_flat[i])

    def neighbors(board, zr, zc, parent_z):
        """Yield (new_board, new_zr, new_zc, move_id) for the four
        possible moves of the blank, skipping the parent
        direction (encoded as the previous (zr, zc))."""
        out = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != parent_z:
                # Move blank from (zr, zc) to (nr, nc).
                new = list(board)
                bi = zr * N + zc
                ni = nr * N + nc
                new[bi], new[ni] = new[ni], new[bi]
                out.append((tuple(new), nr, nc))
        return out

    # Find the blank in start.
    start_flat = tuple(sum(start, []))
    try:
        z0 = start_flat.index(0)
    except ValueError:
        return -1
    zr0, zc0 = z0 // N, z0 % N

    # Each entry: (cost, counter, board_flat, zr, zc, depth, parent_z)
    # cost = depth + misplaced(board). We use a counter to break
    # ties so equal-cost nodes are processed FIFO.
    counter = 0
    pq = [(misplaced(start_flat), 0, start_flat, zr0, zc0, 0, None)]
    seen = {start_flat: 0}  # board_flat -> best depth seen
    while pq:
        cost, _, board, zr, zc, depth, parent_z = heapq.heappop(pq)
        if board == goal_flat:
            return depth
        if seen.get(board, float("inf")) < depth:
            continue
        for new_board, nr, nc in neighbors(board, zr, zc, parent_z):
            new_depth = depth + 1
            if seen.get(new_board, float("inf")) <= new_depth:
                continue
            seen[new_board] = new_depth
            counter += 1
            new_cost = new_depth + misplaced(new_board)
            heapq.heappush(pq, (new_cost, counter, new_board, nr, nc,
                                new_depth, (zr, zc)))
    return -1
