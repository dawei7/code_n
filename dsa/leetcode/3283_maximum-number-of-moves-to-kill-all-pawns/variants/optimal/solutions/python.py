def solve(kx: int, ky: int, positions: list[list[int]]) -> int:
    n = len(positions)
    all_points = [[kx, ky]] + positions
    num_points = len(all_points)

    def knight_distance(a: list[int], b: list[int]) -> int:
        ax, ay = a
        bx, by = b
        corner_pairs = (
            ((0, 0), (1, 1)),
            ((0, 49), (1, 48)),
            ((49, 0), (48, 1)),
            ((49, 49), (48, 48)),
        )
        endpoints = {(ax, ay), (bx, by)}
        if any(endpoints == {p, q} for p, q in corner_pairs):
            return 4

        dx = abs(ax - bx)
        dy = abs(ay - by)
        if dx < dy:
            dx, dy = dy, dx
        if dx == 0 and dy == 0:
            return 0
        if dx == 1 and dy == 0:
            return 3
        if dx == 2 and dy == 2:
            return 4
        moves = max((dx + 1) // 2, (dx + dy + 2) // 3)
        return moves + ((moves + dx + dy) & 1)

    dist = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        for j in range(num_points):
            dist[i][j] = knight_distance(all_points[i], all_points[j])

    memo = {}

    def get_moves(last_idx, mask, turn):
        state = (last_idx, mask, turn)
        if mask == (1 << n) - 1:
            return 0
        if state in memo:
            return memo[state]

        if turn == 0:  # Alice's turn (Maximize)
            res = -float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    res = max(res, dist[last_idx][i + 1] + get_moves(i + 1, mask | (1 << i), 1))
            memo[state] = res
            return res
        else:  # Bob's turn (Minimize)
            res = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    res = min(res, dist[last_idx][i + 1] + get_moves(i + 1, mask | (1 << i), 0))
            memo[state] = res
            return res

    return get_moves(0, 0, 0)
