# Number Letter Counts - Optimal Approach

## Algorithm Explanation

Count total letters in English representations of numbers $1$ to $1000$ (British usage, omitting spaces and hyphens).

1. Define word mapping lookup tables for ones ($1-19$) and tens ($20, 30, \dots, 90$).
2. Recursively convert each number $1 \le n \le 1000$:
   - $n < 20$: lookup in `ONESTR`.
   - $20 \le n < 100$: `TENSSTR[n // 10] + ONESTR[n % 10]`.
   - $100 \le n < 1000$: `ONESTR[n // 100] + "hundred"` plus `"and" + remainder` if non-zero.
   - $n = 1000$: `"onethousand"`.
3. Sum character length `len(words)` across all $1000$ numbers.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000$.
- **Space Complexity:** $\mathcal{O}(1)$ - Fixed lookup tables.
