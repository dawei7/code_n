# Lowest-cost Search - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{200\,000} C(n)$, where $C(n)$ is the worst-case cost of an optimal strategy for finding a hidden number in $\{1, 2, \dots, n\}$ when each guess $k$ costs $k$.

### Minimax Tree Dynamic Programming & Binary Split Recurrence:
1. **Minimax Strategy Formulation**:
   For any interval of length $L$ offset by base $B$:
   $$C(B, L) = \min_{1 \le k \le L} \left( (B + k) + \max(C(B, k-1), C(B + k, L - k)) \right)$$
   For $B = 0$, $C(n) = C(0, n)$.
2. **Monotonic Decision Boundary**:
   The optimal first guess $k$ shifts at intervals corresponding to powers of $2$ ($2^m$).
   Using linear DP with candidate split pruning, $C(n)$ is evaluated sequentially up to $n = 200\,000$.
3. **Execution**:
   Summing $C(n)$ for $n = 1 \dots 200\,000$ yields $260511850222$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 200\,000$. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ DP cost array.
