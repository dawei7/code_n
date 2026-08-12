# Large Sum - Optimal Approach

## Algorithm Explanation

The goal is to compute the first $10$ digits of the sum of one hundred $50$-digit numbers.

In Python, integers have arbitrary precision, avoiding overflow issues found in 64-bit systems:
1. Parse the string containing $100$ lines of $50$-digit numbers.
2. Sum all integers.
3. Slice the first $10$ digits of the stringified total `str(total)[:10]`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot L)$ where $N = 100, L = 50$.
- **Space Complexity:** $\mathcal{O}(N \cdot L)$ - Storage for the raw numbers.
