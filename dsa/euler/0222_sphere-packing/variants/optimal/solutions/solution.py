import math


def solve(pipe_radius: float = 50.0, num_balls: int = 21) -> int:
    """Find minimum length of pipe (in micrometres) containing 21 balls of radii 30mm..50mm.
    
    Time Complexity: O(N^2 * 2^N) for N = 21 (Held-Karp Bitmask DP)
    Space Complexity: O(N * 2^N)
    """
    R = pipe_radius
    N = num_balls
    radii = [30.0 + i for i in range(N)]

    dist = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = math.sqrt(200.0 * (radii[i] + radii[j] - R))

    INF = float('inf')
    num_states = 1 << N
    dp = [[INF] * N for _ in range(num_states)]

    for i in range(N):
        dp[1 << i][i] = radii[i]

    for mask in range(1, num_states):
        for last in range(N):
            if dp[mask][last] == INF:
                continue
            for nxt in range(N):
                if not (mask & (1 << nxt)):
                    next_mask = mask | (1 << nxt)
                    new_cost = dp[mask][last] + dist[last][nxt]
                    if new_cost < dp[next_mask][nxt]:
                        dp[next_mask][nxt] = new_cost

    full_mask = num_states - 1
    min_len = INF
    for last in range(N):
        cost = dp[full_mask][last] + radii[last]
        if cost < min_len:
            min_len = cost

    ans_um = min_len * 1000.0
    return round(ans_um)
