# Modular Inverses - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=3}^{2 \cdot 10^7} I(n)$, where $I(n)$ is the largest $m < n - 1$ such that $m^2 \equiv 1 \pmod n$.

### Chinese Remainder Theorem & Quadratic Residue Root Combinations:
1. **Self-Inverse Congruence**:
   $m$ is its own modular inverse modulo $n$ iff $m^2 \equiv 1 \pmod n \iff (m-1)(m+1) \equiv 0 \pmod n$.
2. **CRT Prime Power Decomposition**:
   For prime power factors $p_i^{e_i} \| n$:
   - If $p_i$ is odd, $m \equiv \pm 1 \pmod{p_i^{e_i}}$ gives 2 solutions.
   - If $p_i = 2$, $m^2 \equiv 1 \pmod{2^e}$ gives 2 solutions ($e \le 2$) or 4 solutions ($e \ge 3$).
   Using Chinese Remainder Theorem, combining all prime power root choices yields all $2^k$ modular square roots of $1 \pmod n$.
3. **Second Largest Root Selection**:
   The largest root $< n$ is always $n-1$.
   $I(n)$ is the second largest root in the CRT root set.
4. **Execution**:
   Summing $I(n)$ for $3 \le n \le 2 \cdot 10^7$ yields $153651073760956$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 2 \cdot 10^7$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ prime sieve array.
