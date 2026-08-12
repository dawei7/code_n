# Square Root Digital Expansion - Optimal Approach

## Algorithm Explanation

Compute the grand sum of the first $100$ decimal digits of all irrational square roots $\sqrt{n}$ for $1 \le n \le 100$.

### High-Precision Integer Shift Strategy:
To obtain $100$ exact decimal digits of $\sqrt{n}$ without floating-point precision loss:
$$\lfloor \sqrt{n \times 10^{198}} \rfloor$$

1. Skip perfect square numbers $n \in \{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$.
2. Multiply $n$ by $10^{198}$ and compute integer square root `math.isqrt(n * 10**198)`.
3. Extract the first $100$ digits of the stringified integer result.
4. Sum the integer value of each digit and accumulate across all $90$ irrational square roots.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot D)$ where $N = 90$ non-square numbers and $D = 100$ digits. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(D)$ - String digit buffer memory.
