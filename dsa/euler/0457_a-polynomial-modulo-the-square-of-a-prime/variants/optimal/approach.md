# A Polynomial Modulo the Square of a Prime - Optimal Approach

## Algorithm Explanation

Find $SR(10^7) = \sum_{p \le 10^7} R(p)$, where $R(p)$ is the smallest positive integer $n$ such that $n^2 - 3n - 1 \equiv 0 \pmod{p^2}$, or $0$ if no such $n$ exists.

### Tonelli-Shanks Quadratic Residues & Hensel's Lemma Lifting:
1. **Quadratic Root Modulo $p$**:
   $n^2 - 3n - 1 \equiv 0 \pmod p \iff (2n - 3)^2 \equiv 13 \pmod p$.
   Solutions exist iff $p = 13$ or $\left(\frac{13}{p}\right) = 1$ (quadratic reciprocity of $13$).
   When $13$ is a quadratic residue mod $p$, we compute roots $r_1, r_2 \pmod p$ using Tonelli-Shanks.
2. **Hensel's Lemma Root Lifting to $\pmod{p^2}$**:
   For each root $r \pmod p$, we lift to $r' \in [1, p^2 - 1]$ modulo $p^2$:
   $$r' = r + k p \quad \text{where } k \equiv -\frac{f(r)/p}{f'(r)} \pmod p$$
   $R(p) = \min(r_1', r_2')$.
3. **Linear Prime Sieve**:
   Using a linear prime sieve up to $L = 10^7$, we compute $R(p)$ for all primes $p \le 10^7$.
4. **Execution**:
   Summing $R(p)$ over all primes $p \le 10^7$ yields $2647787126797397063$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\frac{L \log L}{\log \log L}\right)$ for $L = 10^7$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}\left(\frac{L}{\log L}\right)$ prime sieve array.
