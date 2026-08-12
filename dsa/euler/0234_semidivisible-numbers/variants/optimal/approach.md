# Semidivisible Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all semidivisible numbers $n \le 999966663333$, where $n$ is semidivisible if exactly one of $\operatorname{lps}(n)$ (largest prime $\le \sqrt{n}$) and $\operatorname{ups}(n)$ (smallest prime $\ge \sqrt{n}$) divides $n$.

### Consecutive Prime Interval Arithmetic Progressions:
1. **Interval Property**:
   For any consecutive prime pair $(p_1, p_2)$, all integers $n$ in the open interval $(p_1^2, p_2^2)$ have $\operatorname{lps}(n) = p_1$ and $\operatorname{ups}(n) = p_2$.
2. **Inclusion-Exclusion Summation**:
   Within the interval $[L, R] = [p_1^2 + 1, \min(p_2^2 - 1, N)]$, the sum of semidivisible numbers is:
   $$\text{Sum} = S(p_1, L, R) + S(p_2, L, R) - 2 S(p_1 p_2, L, R)$$
   where $S(k, L, R)$ computes the closed-form sum of multiples of $k$ in $[L, R]$ in $\mathcal{O}(1)$ time.
3. **Execution**:
   Iterating over prime pairs up to $\sqrt{N} \approx 1\,000\,000$ yields total sum $1259187438574927161$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\pi(\sqrt{N})) \approx 78\,498$ iterations. Runs in $\approx 0.12\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{N})$ for prime sieve array.
