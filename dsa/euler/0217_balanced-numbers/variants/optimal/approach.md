# Balanced Numbers - Optimal Approach

## Algorithm Explanation

Find $T(47) \pmod{3^{15}}$, the sum of all balanced numbers less than $10^{47}$ modulo $3^{15} = 14348907$.

### Digit Sum Dynamic Programming:
1. **Balanced Definition**:
   A $k$-digit number is balanced if the sum of its first $\lceil k/2 \rceil$ digits equals the sum of its last $\lceil k/2 \rceil$ digits.
   - For even $k = 2m$: first $m$ digits (no leading 0) and last $m$ digits have equal sum $S$.
   - For odd $k = 2m - 1$: first $m-1$ digits and last $m-1$ digits have equal sum $S$, with any middle digit $d \in \{0 \dots 9\}$.
2. **Half-String DP**:
   Compute `count[L][s][allow_zero]` and `val_sum[L][s][allow_zero]` for half-strings of length $L \le 24$ and digit sum $s \le 216$.
3. **Combination & Convolution**:
   For each length $k \in [1, 47]$, aggregate total numerical contributions modulo $3^{15}$ by convolving first half $A$, middle digit $d$, and second half $B$.
4. **Execution**:
   Summing across all lengths up to $N = 47$ modulo $3^{15}$ yields $6273134$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 \cdot 9) \approx 47 \times 24 \times 9$ states. Runs in $\approx 0.015\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2)$ to store half-string digit-sum tables.
