# Prime Factorisation of Binomial Coefficients - Optimal Approach

## Algorithm Explanation

Find the sum of terms in the prime factorisation of $\binom{20\,000\,000}{15\,000\,000}$, where the sum of terms for $\prod p_i^{e_i}$ is $\sum e_i p_i$.

### Legendre's Formula & Prime Exponent Sieve:
1. **Legendre's Formula**:
   The exponent $e_p(n!)$ of prime $p$ dividing $n!$ is given by:
   $$e_p(n!) = \sum_{j=1}^{\infty} \left\lfloor \frac{n}{p^j} \right\rfloor$$
2. **Binomial Prime Exponents**:
   For $\binom{N}{K} = \frac{N!}{K!(N - K)!}$, the prime exponent $e_p$ of prime $p$ is:
   $$e_p = e_p(N!) - e_p(K!) - e_p((N - K)!)$$
3. **Execution**:
   Sieving all primes $p \le N = 20\,000\,000$ and accumulating $p \times e_p$ yields $7526965179680$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ to sieve primes and sum prime exponents. Runs in $\approx 1.17\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ for prime bytearray sieve.
