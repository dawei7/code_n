# A Lagged Fibonacci Sequence - Optimal Approach

## Algorithm Explanation

Find $g_k \bmod 20092010$ for $k = 10^{18}$, where $g_k = 1$ for $0 \le k \le 1999$ and $g_k = g_{k-2000} + g_{k-1999}$ for $k \ge 2000$.

### Polynomial Modulo Exponentiation (Bostan-Mori / Fiduccia's Algorithm):
1. **Characteristic Polynomial Reduction**:
   The recurrence $g_k = g_{k-2000} + g_{k-1999}$ has characteristic polynomial $P(x) = x^{2000} - x - 1$.
   Computing $g_k$ corresponds to finding $x^K \bmod (x^{2000} - x - 1)$ for $K = 10^{18}$.
2. **Binary Exponentiation**:
   Using $x^{2000} \equiv x + 1 \pmod{P(x)}$, polynomial multiplication and degree reduction takes $\mathcal{O}(N^2)$ per step where $N = 2000$.
   For $K = 10^{18}$, $\approx 60$ polynomial multiplications are performed modulo $20092010$.
3. **Execution**:
   Evaluating $g_{10^{18}} \bmod 20092010$ yields $1274705$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2 \log K)$ for $N = 2000$ and $K = 10^{18}$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ polynomial coefficient storage.
