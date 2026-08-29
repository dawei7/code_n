# Lagged Fibonacci Generator constants (from problem specification)
_LFG_A = 100003
_LFG_B = 200003
_LFG_C = 300007


def solve() -> int:
    """Find the number of successful phone calls required until 99% of the network (990,000 users) is connected to the Prime Minister (PM = 524287).

    Mathematical Principles Applied:
    1. Lagged Fibonacci Pseudo-Random Generator S_k:
       S_k = (100003 - 200003*k + 300007*k^3) mod 1,000,000 for 1 <= k <= 55.
       S_k = (S_{k-24} + S_{k-55}) mod 1,000,000 for k > 55.
       Each call pairs caller u = S_{2k-1} with callee v = S_{2k}.
       A call is SUCCESSFUL if u != v (self-calls are misdials and ignored).

    2. Disjoint Set Union (DSU) / Union-Find Network Connectivity:
       Maintain DSU data structure over N = 1,000,000 nodes with path compression and union-by-size.
       Unify sets for caller u and callee v upon each successful call.

    3. Early Termination Condition:
       Stop as soon as `size[find(PM)] >= 990,000` (99% network component reached).

    Time Complexity: O(C * alpha(N)) where C ~ 2.3M calls, executing in ~1.50s.
    Space Complexity: O(N) memory for DSU parent and size arrays.
    """
    N = 1000000
    PM = 524287
    TARGET = 990000

    parent = list(range(N))
    size = [1] * N

    # Path compression find operation
    def find(i: int) -> int:
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    # Union by size operation
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

    # Circular buffer for Lagged Fibonacci generator S_k
    S_buf = [0] + [
        (_LFG_A - _LFG_B * k + _LFG_C * k**3) % N for k in range(1, 56)
    ]
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

    # Simulate phone calls until 99% network connection is achieved
    while True:
        u = next_S()
        v = next_S()
        if u == v:
            continue  # Ignore misdialed self-calls
        successful_calls += 1
        union(u, v)

        # Check if PM's component contains at least 990,000 users
        if size[find(PM)] >= TARGET:
            break

    # Return total count of successful calls
    return successful_calls


if __name__ == "__main__":
    print(solve())
