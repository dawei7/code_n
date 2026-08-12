# Powerful Digit Sum - Optimal Approach

## Algorithm Explanation

Find the maximum digital sum of $a^b$ for $1 \le a, b < 100$.

Using Python's arbitrary-precision integers:
1. Iterate $a \in [1, 99]$ and $b \in [1, 99]$.
2. Compute $a^b$ in arbitrary precision.
3. Sum the decimal digits of `str(a**b)`.
4. Return the maximum digital sum encountered.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(A \cdot B \cdot D)$ where $A = B = 100$ and $D \le 200$ digits. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(D)$ - String buffer memory.
