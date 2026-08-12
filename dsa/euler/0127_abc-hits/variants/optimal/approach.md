# abc-hits - Optimal Approach

## Algorithm Explanation

Find $\sum c$ for all $c < 120000$ forming an $abc$-hit triplet $(a, b, c)$:
1. $\gcd(a, b) = \gcd(a, c) = \gcd(b, c) = 1$
2. $a < b$
3. $a + b = c$
4. $\operatorname{rad}(abc) < c$

### Radical Multiplicativity & Pruning:
Since $a, b, c$ are pairwise coprime, $\operatorname{rad}(abc) = \operatorname{rad}(a) \operatorname{rad}(b) \operatorname{rad}(c)$.

1. **Precompute Radicals**:
   - Compute $\operatorname{rad}(x)$ for $1 \le x < 120000$ via linear sieve.
2. **Aggressive Pruning Filters**:
   - Since $\operatorname{rad}(a) \ge 1$ and $\operatorname{rad}(b) \ge 1$, $\operatorname{rad}(c) < \frac{c}{2}$. Skip $c$ if $\operatorname{rad}(c) \ge \frac{c}{2}$.
   - For a fixed $c$ and candidate $a$ ($1 \le a < c/2, b = c - a$), test $\operatorname{rad}(a) \operatorname{rad}(b) < \lfloor \frac{c}{\operatorname{rad}(c)} \rfloor$.
   - Evaluate $\gcd(a, b) == 1$ only when radical inequality holds.
3. Accumulate $c$ for all valid $abc$-hits.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \cdot \text{Pruned Candidates})$ where $L = 120000$. Runs in $< 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ - Radical sieve array.
