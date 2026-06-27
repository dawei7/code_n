from collections import deque

def solve(kx: int, ky: int, positions: list[list[int]]) -> int:
    n = len(positions)
    all_points = [[kx, ky]] + positions
    num_points = len(all_points)
    
    # Precompute shortest distances between all pairs using BFS
    dist = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        sx, sy = all_points[i]
        dists = [[-1] * 50 for _ in range(50)]
        dists[sx][sy] = 0
        queue = deque([(sx, sy)])
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < 50 and 0 <= ny < 50 and dists[nx][ny] == -1:
                    dists[nx][ny] = dists[cx][cy] + 1
                    queue.append((nx, ny))
        for j in range(num_points):
            dist[i][j] = dists[all_points[j][0]][all_points[j][1]]
            
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
