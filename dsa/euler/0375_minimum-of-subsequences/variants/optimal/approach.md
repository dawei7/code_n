# Minimum of Subsequences - Optimal Approach

## Algorithm Explanation

We aim to find $M(N) = \sum_{1 \le i \le j \le N} A(i, j)$ for $N = 2\,000\,000\,000$, where $A(i, j) = \min(S_i, \dots, S_j)$ and $S_n$ is produced by $S_0 = 290797, S_{n+1} = S_n^2 \bmod 50515093$.

### Key Mathematical Insights & Algorithm Steps

1. **Monotonic Stack for Subarray Minimums**:
   For any array, we can compute the sum of minimums over all contiguous subarrays ending at index $j$ using a monotonic increasing stack storing $(v, \text{count})$ pairs. At each step $j$, the stack maintains the running sum $E[j] = \sum_{i=1}^j \min(S_i, \dots, S_j)$. The total sum is $\sum_{j=1}^N E[j]$.

2. **Sequence Periodicity**:
   The quadratic PRNG $S_{n+1} = S_n^2 \bmod 50515093$ is purely periodic starting from $n=1$ with period $P = 6\,308\,948$.

3. **Global Minimum Barrier**:
   Within one period of length $P$, the global minimum element is $\min\_val = 3$, occurring uniquely at 1-based index $m = 2\,633\,997$.
   Because $3$ is the absolute minimum of the sequence, whenever the monotonic stack encounters $S_m = 3$, all previous elements in the stack are popped and collapsed into a single base entry $(3, m)$.

4. **Period Extrapolation**:
   By circularly shifting the period $T = S[m+1 \dots P] + S[1 \dots m]$, the global minimum $S_m = 3$ lies at the end of each period.
   - For any period iteration $k$, the local stack state behaves identically over the sequence $T$.
   - The base element $(3, B_k)$ carries a base count $B_k = m + k \cdot P$.
   - The sum over full periods can be computed in $\mathcal{O}(P)$ time by pre-evaluating the local stack sums over $T$ and applying arithmetic series summation for the base contribution.

5. **Final Result**:
   Evaluating $M(2\,000\,000\,000)$ yields $7435327983715286168$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P)$ where $P = 6\,308\,948$. Runs in $\approx 2.3\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ to store sequence $T$ and local stack arrays.

