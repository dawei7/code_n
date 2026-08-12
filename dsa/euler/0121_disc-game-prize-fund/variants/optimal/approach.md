# Disc Game Prize Fund - Optimal Approach

## Algorithm Explanation

Find the maximum integer prize fund allocated for a $15$-turn disc drawing game without expecting a net bank loss.

### Probability DP Model:
At turn $k \in [1, N]$:
- Bag contains $1$ blue disc and $k$ red discs (total $k + 1$ discs).
- $P(\text{Blue}) = \frac{1}{k + 1}$
- $P(\text{Red}) = \frac{k}{k + 1}$

Let $DP[b]$ be the exact rational probability of drawing $b$ blue discs:
1. Base case: $DP[0] = 1$.
2. For $k = 1 \dots N$:
   $$DP_{next}[b] = DP[b] \times \frac{k}{k+1} + DP[b-1] \times \frac{1}{k+1}$$
3. Winning condition: Player draws strictly more blue discs than red discs ($b \ge \lfloor N/2 \rfloor + 1 = 8$).
4. Total winning probability $P_{win} = \sum_{b=8}^{15} DP[b]$.
5. Maximum prize fund = $\lfloor \frac{1}{P_{win}} \rfloor$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 15$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Rational DP array.
