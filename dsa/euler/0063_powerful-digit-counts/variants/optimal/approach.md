# Powerful Digit Counts - Optimal Approach

## Algorithm Explanation

Count how many $n$-digit positive integers exist which are also an $n^{\text{th}}$ power ($x = a^n$ has length $n$).

### Mathematical Bounds
1. **Base $a < 10$**: $10^n$ has $n + 1$ digits for all $n \ge 1$. Any $a \ge 10$ yields $a^n \ge 10^n$ ($> n$ digits). Thus $1 \le a \le 9$.
2. **Exponent $n$ Upper Bound**: An $n$-digit number satisfies $10^{n-1} \le a^n < 10^n$.
   Taking logarithms:
   $$n - 1 \le n \log_{10}(a) \implies n(1 - \log_{10}(a)) \le 1 \implies n \le \frac{1}{1 - \log_{10}(a)}$$
   For $a = 9$, $n \le 21$.

### Strategy:
- Loop $a \in [1, 9]$ and $n = 1, 2 \dots$ while $\text{len}(\text{str}(a^n)) == n$.
- Increment and return total count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Fixed maximum bound ($9 \times 22$ iterations). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
