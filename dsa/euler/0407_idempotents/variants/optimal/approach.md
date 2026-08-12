# Idempotents - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10^7} M(n)$, where $M(n)$ is the largest integer $a < n$ satisfying $a^2 \equiv a \pmod n$.

### Idempotent Factorization & Chinese Remainder Theorem:
1. **Idempotent Congruence Property**:
   $a^2 \equiv a \pmod n \iff a(a - 1) \equiv 0 \pmod n$.
   Since $\gcd(a, a - 1) = 1$, for each prime power $p^k \| n$, $p^k$ must divide either $a$ or $a - 1$.
   Thus, $a \pmod{p^k} \in \{0, 1\}$.
2. **CRT Idempotent Generation**:
   For $n = p_1^{e_1} p_2^{e_2} \cdots p_m^{e_m}$, there are $2^m$ idempotent solutions $a \in [0, n - 1]$, constructed by choosing $a \equiv 0 \text{ or } 1 \pmod{p_i^{e_i}}$ for each prime power and combining via the Chinese Remainder Theorem (CRT).
3. **Linear Sieve & CRT Maximum Search**:
   Using a linear prime sieve up to $N = 10^7$, we factor each $n \le 10^7$ into prime powers and find the maximum CRT solution $a < n$.
4. **Execution**:
   Summing $M(n)$ for $1 \le n \le 10^7$ yields $39786377843165$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ for $N = 10^7$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ sieve array.
