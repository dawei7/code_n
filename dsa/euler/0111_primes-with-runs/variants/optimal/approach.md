# Primes with Runs - Optimal Approach

## Algorithm Explanation

Find the sum of all $S(10, d)$ for digits $d \in [0, 9]$, where $S(10, d)$ is the sum of all $10$-digit prime numbers containing the maximum possible number of repeated digits $M(10, d)$.

### Search & Verification Strategy:
For each target repeated digit $d \in [0, 9]$:
1. Search $m = 9$ down to $1$ for the maximum count of repeated digits $d$.
2. Choose $m$ positions out of $10$ for digit $d$ ($\binom{10}{m}$ choices).
3. Fill the remaining $10 - m$ positions with non-$d$ digits from $\{0 \dots 9\} \setminus \{d\}$.
4. Reject candidate numbers with leading zero (`digits[0] == 0`).
5. Perform deterministic **Miller-Rabin Primality Testing** on candidate integers.
6. Once any primes are discovered for a given count $m$:
   - Set $M(10, d) = m$.
   - Calculate $S(10, d) = \sum \text{Primes}$.
   - Terminate search for digit $d$.
7. Sum $S(10, d)$ over all digits $d = 0 \dots 9$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D \cdot \binom{10}{m} \cdot 9^{10-m} \cdot \log^3 N)$ where $m \ge 8$. Runs in $< 0.12\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ - Unique prime accumulator list.
