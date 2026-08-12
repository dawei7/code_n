# Reciprocal Cycles - Optimal Approach

## Algorithm Explanation

The decimal expansion of a unit fraction $\frac{1}{d}$ repeats when a long-division remainder re-occurs.

1. Track remainders $r_0 = 1, r_{i+1} = (10 r_i) \bmod d$.
2. Store remainder positions in a map `seen[remainder] = position`.
3. When $r_i$ repeats, cycle length is $i - \text{seen}[r_i]$.
4. Iterate $d$ downwards from $N - 1$ to $2$.
5. **Pruning**: Since cycle length $L(d) < d$, if $d \le \text{max\_cycle\_found}$, we break immediately.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D^2)$ where $D = 1000$. With downward iteration pruning, runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(D)$ - Auxiliary hash map for remainders.
