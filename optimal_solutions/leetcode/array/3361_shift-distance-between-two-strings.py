def solve(s: str, t: str, nextCost: list[int], prevCost: list[int]) -> int:
    # Precompute the minimum cost to go from any char i to any char j
    # There are 26 characters.
    # dist[i][j] is the min cost to transform char i to char j
    
    n = 26
    # Forward prefix sums for nextCost
    # fwd_pref[i] is cost to go from 0 to i moving forward
    fwd_pref = [0] * (n + 1)
    for i in range(n):
        fwd_pref[i + 1] = fwd_pref[i] + nextCost[i]
        
    # Backward prefix sums for prevCost
    # bwd_pref[i] is cost to go from 0 to i moving backward
    # Note: moving backward from i to i-1 is prevCost[i]
    bwd_pref = [0] * (n + 1)
    for i in range(n):
        bwd_pref[i + 1] = bwd_pref[i] + prevCost[(n - i) % n]
        
    def get_cost(start: int, end: int) -> int:
        if start == end:
            return 0
        
        # Option 1: Move forward from start to end
        if end > start:
            fwd = fwd_pref[end] - fwd_pref[start]
        else:
            fwd = (fwd_pref[n] - fwd_pref[start]) + fwd_pref[end]
            
        # Option 2: Move backward from start to end
        if end < start:
            bwd = bwd_pref[start - end]
        else:
            bwd = bwd_pref[start + (n - end)]
            
        return min(fwd, bwd)

    total_cost = 0
    for char_s, char_t in zip(s, t):
        u = ord(char_s) - ord('a')
        v = ord(char_t) - ord('a')
        total_cost += get_cost(u, v)
        
    return total_cost
