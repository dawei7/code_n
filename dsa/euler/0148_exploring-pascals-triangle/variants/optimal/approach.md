# Exploring Pascal's Triangle - Optimal Approach

## Algorithm Explanation

Find the number of entries in the first $10^9$ rows ($n = 0 \dots 10^9 - 1$) of Pascal's triangle that are **not** divisible by $7$.

### Lucas' Theorem & Base-$7$ Fractal Reduction:
By Lucas' Theorem, a binomial coefficient $\binom{n}{k} \not\equiv 0 \pmod 7$ if and only if every base-$7$ digit of $k$ is less than or equal to the corresponding base-$7$ digit of $n$.

The number of non-zero entries modulo $7$ in row $n$ is:
$$f(n) = \prod_{i=0}^d (n_i + 1)$$
where $(n_d, \dots, n_0)_7$ is the base-$7$ representation of $n$.

### Recursive Digit Accumulation:
To sum $f(n)$ for $0 \le n < N$:
Express $N$ in base $7$ with top digit $d$ at position $k$ ($7^k \le N < 7^{k+1}$):
1. **Full Sub-Pyramid Blocks**:
   The $d$ complete blocks of size $7^k$ contribute:
   $$\text{Full}(N) = \frac{d(d+1)}{2} \times 28^k$$
2. **Partial Sub-Pyramid Block**:
   The remaining rows $N \bmod 7^k$ have their top digit fixed as $d$, contributing:
   $$\text{Partial}(N) = (d + 1) \times \operatorname{Count}(N \bmod 7^k)$$

Evaluate recursively in $\mathcal{O}(\log_7 N)$ steps.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_7 N)$ where $N = 10^9$ ($\le 11$ recursive steps). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log_7 N)$ - Recursion stack memory.
