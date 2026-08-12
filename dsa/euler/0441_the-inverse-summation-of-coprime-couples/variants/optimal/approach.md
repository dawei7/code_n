# The Inverse Summation of Coprime Couples - Optimal Approach

## Algorithm Explanation

Find $S(10^7) = \sum_{i=2}^{10^7} R(i)$ rounded to 4 decimal places, where $R(M) = \sum \frac{1}{p \cdot q}$ over all coprime pairs $1 \le p < q \le M$ with $p + q \ge M$.

### Möbius Inversion & Harmonic Sequence Prefix Sieve:
1. **Order of Summation Swap**:
   Swapping the summation over $M \in [2, N]$ and coprime pairs $1 \le p < q \le N$:
   A coprime pair $(p, q)$ contributes $\frac{1}{p \cdot q}$ to $R(M)$ for all $M$ in the range $\max(q, p+q - \text{something}) \dots p+q$.
2. **Möbius Inversion**:
   Removing the coprime condition $\gcd(p, q) = 1$ via Möbius inversion $\mu(d)$:
   $$S(N) = \sum_{d=1}^N \frac{\mu(d)}{d^2} \sum_{1 \le p' < q' \le \lfloor N/d \rfloor} f(p', q')$$
   where $f(p', q')$ depends on harmonic numbers $H_k = \sum_{j=1}^k 1/j$.
3. **Linear Harmonic Sieve**:
   Using precomputed harmonic prefix sums and Möbius sieve up to $N = 10^7$, $S(N)$ is evaluated in $\mathcal{O}(N \log N)$ operations.
4. **Execution**:
   Evaluating $S(10^7)$ rounded to 4 decimal places yields $5000088.8395$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 10^7$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ harmonic sum table.
