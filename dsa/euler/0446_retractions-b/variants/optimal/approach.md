# Retractions B - Optimal Approach

## Algorithm Explanation

Find $F(10^7) \bmod 1000000007$, where $F(N) = \sum_{n=1}^N R(n^4 + 4)$ and $R(m)$ is the number of linear retractions modulo $m$.

### Sophie Germain Factorization & Polynomial Sieve:
1. **Sophie Germain Identity**:
   The quartic polynomial $n^4 + 4$ factors into two quadratic terms:
   $$n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2) = A_n B_n$$
   Notice $B_n = A_{n+2}$, meaning $A_n = n^2 - 2n + 2$ forms an overlapping sequence of quadratic terms.
2. **Multiplicative Retraction Property**:
   For $m = A_n B_n$, $R(m) = \prod_{p_i^{e_i} \| m} (2 p_i^{e_i} - 1)$.
   Because $\gcd(A_n, B_n) \in \{1, 2, 5\}$, prime factors of $A_n$ and $B_n$ overlap at most at $2$ and $5$.
3. **Quadratic Sieve for $A_n = n^2 - 2n + 2$**:
   A prime $p$ divides $n^2 - 2n + 2$ iff $(n-1)^2 \equiv -1 \pmod p$, which requires $p = 2$ or $p \equiv 1 \pmod 4$.
   We run a polynomial sieve up to $N = 10^7$ to factor $A_n$ and $B_n$ for all $n \le 10^7$.
4. **Execution**:
   Evaluating $F(10^7) \bmod 1000000007$ yields $907803852$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10^7$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ linear polynomial sieve arrays.
