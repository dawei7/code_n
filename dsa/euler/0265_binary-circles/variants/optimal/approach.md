# Binary Circles - Optimal Approach

## Algorithm Explanation

Find $S(5)$, the sum of all unique numeric representations of De Bruijn binary circles of order $N = 5$ (circular sequences of length $2^5 = 32$ where all $5$-digit clockwise subsequences are distinct, starting with $00000$).

### Backtracking Depth-First Search with Bitmask Tracking:
1. **Canonical Start**:
   Without loss of generality, every De Bruijn sequence starts with $N = 5$ zeros ($00000$).
   The initial subsequence $00000_2 = 0$ is marked as visited in a bitmask.
2. **Backtracking Branching**:
   At step $k$ ($N \le k < 32$), we append bit $b \in \{0, 1\}$.
   The new $5$-bit subsequence is `next_subseq = ((current_subseq << 1) & 31) | b`.
   If `next_subseq` has not been visited, we recurse.
3. **Circular Boundary Wrapping Validation**:
   When the length reaches $32$, we validate the $N-1 = 4$ wrapping subsequences formed by ending bits and leading zeros.
   If all $32$ subsequences are unique, we convert the binary string to an integer and accumulate it.
4. **Execution**:
   Summing all valid binary circle representations for $N = 5$ yields $209110240768$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^{2^N})$ pruned DFS over De Bruijn cycles. Runs in $\approx 0.04\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^N)$ bitmask and stack depth.
