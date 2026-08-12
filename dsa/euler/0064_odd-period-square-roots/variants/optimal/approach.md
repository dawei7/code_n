# Odd Period Square Roots - Optimal Approach

## Algorithm Explanation

Determine how many continued fraction expansions of $\sqrt{N}$ for non-square $N \le 10000$ have an odd period length.

### Continued Fraction State Recurrence
For $\sqrt{N}$ with initial integer component $a_0 = \lfloor \sqrt{N} \rfloor$:
State variables start at $m_0 = 0, d_0 = 1, a_0 = \lfloor \sqrt{N} \rfloor$.

At step $k$:
1. $m_{k+1} = d_k \cdot a_k - m_k$
2. $d_{k+1} = \frac{N - m_{k+1}^2}{d_k}$
3. $a_{k+1} = \lfloor \frac{a_0 + m_{k+1}}{d_{k+1}} \rfloor$

The periodic expansion repeats as soon as $a_{k+1} = 2 a_0$.
Count all non-square $N \le 10000$ whose period length $k+1$ is odd.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot P)$ where $N = 10000$ and $P \le 250$. Runs in $< 0.08\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
