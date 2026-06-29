def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(data[index])
        index += 1
        M = int(data[index])
        index += 1
        cuts = list(map(int, data[index:index + M]))
        index += M
        points = [0] + cuts + [N]
        m_ext = len(points)
        dp = [[(0, []) for _ in range(m_ext)] for __ in range(m_ext)]
        for gap in range(2, m_ext):
            for i in range(m_ext - gap):
                j = i + gap
                best_cost = None
                best_seq = None
                for k in range(i + 1, j):
                    cost_left, seq_left = dp[i][k]
                    cost_right, seq_right = dp[k][j]
                    cost_here = points[j] - points[i]
                    candidate_cost = cost_left + cost_right + cost_here
                    candidate_seq = [points[k]] + seq_left + seq_right
                    if best_cost is None or candidate_cost < best_cost:
                        best_cost = candidate_cost
                        best_seq = candidate_seq
                    elif candidate_cost == best_cost:
                        if candidate_seq < best_seq:
                            best_seq = candidate_seq
                dp[i][j] = (best_cost, best_seq)
        order = dp[0][m_ext - 1][1]
        results.append(' '.join(map(str, order)) + ' ')
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
