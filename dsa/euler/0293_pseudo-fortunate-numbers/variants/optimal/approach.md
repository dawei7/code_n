# Pseudo-Fortunate Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all distinct pseudo-Fortunate numbers $M$ for admissible numbers $N < 10^9$. An admissible number $N$ is even with prime factors consisting of consecutive primes starting at $2$. $M > 1$ is the smallest integer such that $N + M$ is prime.

### Admissible Generator & Primality Search:
1. **Admissible Number Generation**:
   Starting with $N = 2$, admissible numbers are generated recursively by either multiplying by the current prime factor or introducing the next consecutive prime ($3, 5, 7, \dots$).
   There are only $6656$ admissible numbers $N < 10^9$.
2. **Pseudo-Fortunate Evaluation**:
   For each admissible $N$, we test odd values $M = 3, 5, 7, \dots$ until $N + M$ is prime (using deterministic Miller-Rabin test).
3. **Execution**:
   Collecting the set of distinct pseudo-Fortunate values $M$ across all $6656$ admissible numbers and summing them yields $2209$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot G)$ where $K = 6656$ admissible numbers and $G$ is the average prime gap. Runs in $\approx 0.08\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ for admissible numbers set.
