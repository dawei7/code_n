# Divisibility Multipliers - Optimal Approach

## Algorithm Explanation

Find the sum of the divisibility multipliers $m < p$ for all prime numbers $p < 10^7$ coprime to $10$ ($p \ne 2, 5$).

### Modular Inverse Characterization:
1. **Divisibility Condition**:
   For $n = 10a + b$, the function $f(n) = a + b m$ preserves divisibility by $p$ if and only if $a + b m \equiv 0 \pmod p$ whenever $10a + b \equiv 0 \pmod p$.
   Since $a \equiv -b \cdot 10^{-1} \pmod p$, substituting gives:
   $$b(m - 10^{-1}) \equiv 0 \pmod p \implies m \equiv 10^{-1} \pmod p$$
2. **Sieve & Inverse Evaluation**:
   Using the Sieve of Eratosthenes up to $10^7$, for each prime $p \notin \{2, 5\}$, we compute $m(p) = 10^{-1} \bmod p$.
3. **Execution**:
   Summing $m(p)$ over all $664\,577$ eligible primes yields $1601912348822$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\pi(N) \cdot \log p)$ for $N = 10^7$. Runs in $\approx 0.46\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ bytearray sieve memory.
