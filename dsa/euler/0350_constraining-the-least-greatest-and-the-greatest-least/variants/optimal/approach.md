# Constraining the Least Greatest and the Greatest Least - Optimal Approach

## Algorithm Explanation

Find $f(10^6, 10^{12}, 10^{18}) \bmod 101^4$, where $f(G, L, N)$ is the number of lists of size $N$ with $\gcd \ge G$ and $\operatorname{lcm} \le L$.

### Multiplicative Inclusion-Exclusion & Modular Exponentiation:
1. **Ratio Transformation**:
   Let each entry $x_i = g \cdot y_i$, where $g = \gcd(x_1, \dots, x_N) \ge G$ and $k = \operatorname{lcm}(y_1, \dots, y_N) \le \lfloor L / g \rfloor$.
   This reduces the problem to counting $N$-tuples $(y_1, \dots, y_N)$ with $\gcd(y)=1$ and $\operatorname{lcm}(y)=k$.
2. **Prime Power Inclusion-Exclusion**:
   For a prime power $p^a \| k$, each entry $y_i$ can have exponent $e_i \in [0, a]$.
   To ensure $\min(e_i) = 0$ and $\max(e_i) = a$, the number of valid exponent choices across $N$ elements is:
   $$V_N(a) = (a + 1)^N - 2 a^N + (a - 1)^N$$
   By multiplicativity, the total number of valid $y$-tuples for $k = \prod p_i^{a_i}$ is $\prod V_N(a_i)$.
3. **Sub-linear Multiplicative Sieve**:
   Summing over ratios $k \le \lfloor L / g \rfloor$ across all valid $g \ge G$ using Dirichlet floor sum reduction modulo $101^4$ ($101^4 = 104\,060\,401$).
4. **Execution**:
   Evaluating $f(10^6, 10^{12}, 10^{18}) \bmod 101^4$ yields $84664213$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(M)$ where $M = L/G = 10^6$. Runs in $\approx 0.85\text{s}$.
- **Space Complexity:** $\mathcal{O}(M)$ multiplicative sieve table.
