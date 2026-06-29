


def solve():
    def countDistinctInSubmatrix(N: int, A: list[list[int]], Q: int, queries: list[list[int]]) -> list[int]:
        # 3D prefix sum table initialized to 0
        pref = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(11)]

        for v in range(1, 11):
            p_v = pref[v]
            for i in range(1, N + 1):
                p_v_i = p_v[i]
                p_v_prev = p_v[i - 1]
                A_row = A[i - 1]
                for j in range(1, N + 1):
                    val = 1 if A_row[j - 1] == v else 0
                    p_v_i[j] = val + p_v_prev[j] + p_v_i[j - 1] - p_v_prev[j - 1]

        ans = []
        for x1, y1, x2, y2 in queries:
            distinct_count = 0
            for v in range(1, 11):
                p_v = pref[v]
                count = p_v[x2][y2] - p_v[x1 - 1][y2] - p_v[x2][y1 - 1] + p_v[x1 - 1][y1 - 1]
                if count > 0:
                    distinct_count += 1
            ans.append(distinct_count)

        return ans


if __name__ == "__main__":
    solve()
