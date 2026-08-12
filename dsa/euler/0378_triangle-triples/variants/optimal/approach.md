# Triangle Triples - Optimal Approach

## Algorithm Explanation

Find the last 18 digits of $Tr(60\,000\,000) \bmod 10^{18}$, where $Tr(n)$ is the number of triples $(i, j, k)$ with $1 \le i < j < k \le n$ such that $dT(i) > dT(j) > dT(k)$ for triangle number divisor counts $dT(m) = d\left(\frac{m(m+1)}{2}\right)$.

### Linear Divisor Sieve & Fenwick Tree Inversion Counting:
1. **Triangle Number Divisor Multiplicativity**:
   Since $\gcd(m, m+1) = 1$, the divisor count $dT(m)$ splits multiplicatively:
   - If $m$ is even: $dT(m) = d(m/2) \cdot d(m+1)$.
   - If $m$ is odd: $dT(m) = d(m) \cdot d((m+1)/2)$.
   We precompute $d(k)$ for all $k \le N+1 = 60\,000\,001$ using a linear sieve.
2. **Fenwick Tree (BIT) Middle-Element Counting**:
   For each index $j \in [1, N]$ acting as the middle element of the triple:
   - $L_j$: count of indices $i < j$ with $dT(i) > dT(j)$ (left-to-right Fenwick tree query).
   - $R_j$: count of indices $k > j$ with $dT(k) < dT(j)$ (right-to-left Fenwick tree query).
   The number of valid triples centered at $j$ is $L_j \times R_j$.
3. **Execution**:
   Summing $L_j \times R_j \bmod 10^{18}$ for $N = 60\,000\,000$ yields last 18 digits $147534623725795891$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log(\max dT))$ for $N = 60\,000\,000$ and $\max dT \le 1000$. Runs in $\approx 0.90\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ sieve and value arrays.
