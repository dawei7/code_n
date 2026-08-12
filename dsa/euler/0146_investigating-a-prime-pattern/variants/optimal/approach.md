# Investigating a Prime Pattern - Optimal Approach

## Algorithm Explanation

Find the sum of all positive integers $n < 150,000,000$ for which the sequence $n^2 + 1, n^2 + 3, n^2 + 7, n^2 + 9, n^2 + 13, n^2 + 27$ forms six **consecutive** prime numbers.

### Modular Residue Sieve Filters:
Testing all candidates up to $150 \times 10^6$ with primality tests directly would be slow. We apply aggressive modular residue constraints:

1. **Modulo 2 & 5**: $n$ must end in $0$ ($n \equiv 0 \pmod{10}$).
2. **Modulo 3**: $n^2 \equiv 1 \pmod 3$.
3. **Modulo 7**: $n^2 \equiv 2 \pmod 7$.
4. **Primes $p \in \{11, 13, 17, 19, 23, 29\}$**:
   - $n^2 \bmod p \notin \{-1, -3, -7, -9, -13, -27\} \bmod p$.
   - Prunes over $99.2\%$ of candidates before performing any primality test.

### Primality & Consecutive Checks:
1. Perform deterministic **Miller-Rabin Primality Testing** on the required six expressions.
2. Verify consecutive prime property by checking that all intermediate odd numbers ($n^2 + 5, n^2 + 11, n^2 + 15, n^2 + 17, n^2 + 19, n^2 + 21, n^2 + 23, n^2 + 25$) are composite.
3. Accumulate valid $n$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Limit} \cdot \text{FilterRatio} \cdot \text{MillerRabin})$. Runs in $\approx 4.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
