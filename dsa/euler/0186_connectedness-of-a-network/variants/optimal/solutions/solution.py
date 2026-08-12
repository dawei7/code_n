def solve() -> int:
    """Find number of successful calls until 99% of network connected to PM.
    
    Time Complexity: O(C * alpha(N)) where C ~ 2.3M calls, alpha is inverse Ackermann
    Space Complexity: O(N) where N = 1,000,000 users
    """
    N = 1000000
    PM = 524287
    TARGET = 990000

    parent = list(range(N))
    size = [1] * N

    def find(i: int) -> int:
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    def union(i: int, j: int) -> bool:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    S_buf = [0] + [(100003 - 200003 * k + 300007 * k**3) % N for k in range(1, 56)]
    k_idx = 1

    def next_S() -> int:
        nonlocal k_idx
        if k_idx <= 55:
            val = S_buf[k_idx]
            k_idx += 1
            return val
        else:
            idx_24 = (k_idx - 24 - 1) % 55 + 1
            idx_55 = (k_idx - 55 - 1) % 55 + 1
            val = (S_buf[idx_24] + S_buf[idx_55]) % N
            S_buf[idx_55] = val
            k_idx += 1
            return val

    successful_calls = 0
    while True:
        u = next_S()
        v = next_S()
        if u == v:
            continue
        successful_calls += 1
        union(u, v)

        if size[find(PM)] >= TARGET:
            break

    return successful_calls
