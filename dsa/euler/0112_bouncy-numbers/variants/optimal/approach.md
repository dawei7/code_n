# Bouncy Numbers - Optimal Approach

## Algorithm Explanation

Find the least integer $n$ for which the proportion of bouncy numbers first reaches exactly $99\%$ ($100 \times \text{bouncy\_count} = 99 \times n$).

### Definitions:
- **Increasing**: Digit sequence left-to-right never decreases ($d_i \le d_{i+1}$).
- **Decreasing**: Digit sequence left-to-right never increases ($d_i \ge d_{i+1}$).
- **Bouncy**: Neither increasing nor decreasing (contains both an increase $d_i < d_{i+1}$ and a decrease $d_j > d_{j+1}$).

### Strategy:
1. Increment $n = 100, 101 \dots$.
2. Check bounciness in a single pass over digits of $str(n)$, stopping early as soon as both `inc` and `dec` flags become true.
3. Update cumulative `bouncy_count`.
4. Return $n$ when $100 \times \text{bouncy\_count} = 99 \times n$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot D)$ where $N = 1587000$ and $D \le 7$ digits. Runs in $< 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
