def solve(limit: int = 200) -> int:
    """Find sum of minimal multiplications m(k) for 1 <= k <= 200 using Addition Chain IDDFS.
    
    Time Complexity: O(IDDFS)
    Space Complexity: O(Depth)
    """
    min_mults = [float('inf')] * (limit + 1)
    min_mults[1] = 0

    def dfs(chain: list[int], depth: int, max_depth: int):
        curr = chain[-1]

        if curr <= limit and depth < min_mults[curr]:
            min_mults[curr] = depth

        if depth == max_depth:
            return

        # Star-chain additions: combine current element with elements in chain
        for prev in reversed(chain):
            nxt = curr + prev
            if nxt <= limit and nxt > curr:
                dfs(chain + [nxt], depth + 1, max_depth)

    # Iterative Deepening DFS
    max_d = 1
    while any(min_mults[k] == float('inf') for k in range(1, limit + 1)):
        dfs([1], 0, max_d)
        max_d += 1

    return sum(min_mults[1:limit + 1])
