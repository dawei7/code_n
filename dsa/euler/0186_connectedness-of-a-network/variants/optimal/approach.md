# Connectedness of a Network - Optimal Approach

## Algorithm Explanation

Determine after how many successful phone calls (excluding misdials where caller = called) at least $99\%$ ($990,000$) of $1,000,000$ users belong to the same connected component as the Prime Minister (User ID $524287$).

### Lagged Fibonacci Generator & Disjoint Set Union:
1. **LFG Stream Generation**:
   Phone numbers are generated in pairs $(S_{2n-1}, S_{2n})$ using:
   - $S_k = (100003 - 200003k + 300007k^3) \pmod{10^6}$ for $1 \le k \le 55$.
   - $S_k = (S_{k-24} + S_{k-55}) \pmod{10^6}$ for $k \ge 56$.
   We generate numbers lazily using a circular buffer of size $55$.
2. **Disjoint Set Union (DSU / Union-Find)**:
   Maintain disjoint sets over $1,000,000$ nodes with path compression and union by size.
   For each call $(u, v)$:
   - If $u = v$, skip (misdial).
   - Increment `successful_calls`.
   - Perform `union(u, v)`.
   - Check if `size[find(PM)] >= 990000`.
3. **Termination**:
   The threshold is reached at exactly $2,325,629$ successful calls.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(C \cdot \alpha(N))$ where $C \approx 2.3\times 10^6$ calls, $N = 10^6$, and $\alpha$ is the inverse Ackermann function. Runs in $\approx 4.3\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Parent and size arrays for DSU.
