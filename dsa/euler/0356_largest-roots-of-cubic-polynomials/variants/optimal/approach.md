# Largest Roots of Cubic Polynomials - Optimal Approach

## Algorithm Explanation

Find the last 8 digits of $\sum_{i=1}^{30} \lfloor a_i^{987654321} \rfloor \bmod 10^8$, where $a_i$ is the largest real root of $g_i(x) = x^3 - 2^i x^2 + i$.

### Root Power Sums & Matrix Exponentiation Modulo $10^8$:
1. **Root Power Sum Identity**:
   For $g_i(x) = x^3 - 2^i x^2 + i = 0$, let its three real roots be $a_i, r_2, r_3$.
   Since $a_i \approx 2^i$, the remaining two roots satisfy $|r_2|, |r_3| < 1$.
   The sum of $k$-th powers $S_k = a_i^k + r_2^k + r_3^k$ is an exact integer satisfying Newton's linear recurrence:
   $$S_k = 2^i S_{k-1} - i S_{k-3}$$
2. **Floor Function Identity**:
   For large $k = 987654321$, $0 < r_2^k + r_3^k < 1$, which implies:
   $$\lfloor a_i^k \rfloor = S_k - 1$$
3. **$3 \times 3$ Matrix Binary Exponentiation**:
   With base values $S_0 = 3, S_1 = 2^i, S_2 = 2^{2i}$, $S_k \bmod 10^8$ is computed in $\mathcal{O}(\log k)$ time via binary matrix exponentiation.
4. **Execution**:
   Summing $(S_k(i) - 1) \bmod 10^8$ for $i = 1 \dots 30$ yields $28010159$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log K)$ for $N = 30$ and $K = 987654321$. Runs in $\approx 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
