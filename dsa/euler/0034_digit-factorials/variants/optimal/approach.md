# Digit Factorials - Optimal Approach

## Algorithm Explanation

Find all numbers $N \ge 10$ equal to the sum of the factorials of their decimal digits.

### Upper Bound Derivation
For a $D$-digit number, maximum digit factorial sum is $D \times 9! = D \times 362880$.
- $D = 7$: $7 \times 362880 = 2540160$ ($7$-digit upper limit).
- $D = 8$: $8 \times 362880 = 2903040 < 10^7$ ($7$-digit maximum, strictly smaller than any $8$-digit number).
Hence no solution exists above $7 \times 9! = 2540160$.

### Search Strategy:
1. Precompute `facts[d] = d!` for $0 \le d \le 9$.
2. Iterate $i$ from $10$ to $2540160$.
3. Check $i = \sum \text{facts}[\text{int}(c)]$ for $c \in \text{str}(i)$.
4. Sum all matching numbers.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \log_{10} L)$ where $L = 2540160$. Runs in $< 0.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Fixed factorial lookup array.
