# Modular Cubes, Part 1 - Optimal Approach

## Algorithm Explanation

Find $S(N)$, the sum of all integers $1 < x < N$ satisfying $x^3 \equiv 1 \pmod N$ for $N = 13082761331670030$.

### Chinese Remainder Theorem (CRT) Modular Combination:
1. **Prime Factorization**:
   $N = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 \times 23 \times 29 \times 31 \times 37 \times 41 \times 43$ (product of first 14 primes).
2. **Local Modular Cube Roots**:
   By CRT, $x^3 \equiv 1 \pmod N \iff x^3 \equiv 1 \pmod p$ for each prime factor $p$.
   - For primes $p \equiv 1 \pmod 3$ ($7, 13, 19, 31, 37, 43$), there are $3$ cube roots modulo $p$.
   - For all other primes, there is $1$ unique root ($x \equiv 1 \pmod p$).
3. **Cartesian Product & Reconstruction**:
   There are $3^6 = 729$ total solutions modulo $N$. We construct all $729$ solutions via CRT.
4. **Execution**:
   Excluding $x = 1$, summing the remaining $728$ values yields $4617456485273129588$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(3^k)$ where $k = 6$ primes $\equiv 1 \pmod 3$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(3^k)$ CRT list.
