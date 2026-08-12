# Digit Fifth Powers - Optimal Approach

## Algorithm Explanation

Find all numbers greater than $1$ equal to the sum of the fifth powers of their decimal digits.

### Upper Bound Derivation
For a $D$-digit number, the maximum digit fifth-power sum is $D \times 9^5 = D \times 59049$.
- For $D = 6$, $6 \times 59049 = 354294$ ($6$ digits).
- For $D = 7$, $7 \times 59049 = 413343 < 10^6$ ($6$ digits, strictly smaller than a $7$-digit number).
Hence, no solution can exceed $6 \times 9^5 = 354294$.

### Search Strategy:
1. Precompute powers array `powers[d] = d^5` for $0 \le d \le 9$.
2. Iterate $i$ from $10$ to $354294$.
3. Sum `powers[int(c)]` for each character $c$ in $\text{str}(i)$.
4. Accumulate and return matching values.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \log_{10} L)$ where $L = 354294$. Runs in under $0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Fixed power lookup table.
