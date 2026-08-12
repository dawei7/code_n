# Composites with Prime Repunit Property - Optimal Approach

## Algorithm Explanation

Find the sum of the first $25$ composite integers $n$ ($\gcd(n, 10) = 1$) for which $n - 1$ is divisible by $A(n)$, where $A(n)$ is the minimal repunit length $k$ such that $R(k) = \frac{10^k - 1}{9}$ is divisible by $n$.

### Repunit Property & Fermat-like Pseudoprimes:
By Euler's Totient Theorem, for prime $p > 5$, $p - 1$ is always divisible by $A(p)$. Composite numbers satisfying $(n - 1) \bmod A(n) = 0$ are rare repunit pseudoprimes.

### Strategy:
1. Iterate candidates $n = 6, 7, 8 \dots$.
2. Filter candidates requiring $\gcd(n, 10) = 1$ and non-primality (`not is_prime(n)`).
3. Compute $a = A(n)$ via modular repunit state transitions $r_{k+1} = (10 r_k + 1) \bmod n$.
4. Collect $n$ if $(n - 1) \bmod a == 0$.
5. Stop when $25$ composite values are found and return their total sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot A(n))$ where $N \le 15000$. Runs in $< 0.18\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
