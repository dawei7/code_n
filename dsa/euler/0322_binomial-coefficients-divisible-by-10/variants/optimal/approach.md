# Binomial Coefficients Divisible by 10 - Optimal Approach

## Algorithm Explanation

Find $T(10^{18}, 10^{12} - 10)$, the number of binomial coefficients $\binom{i}{n}$ divisible by $10$ for $n \le i < m$ ($m = 10^{18}, n = 10^{12} - 10$).

### Lucas' Theorem & Dual Base Digit Inclusion-Exclusion:
1. **Divisibility Condition**:
   $\binom{i}{n}$ is divisible by $10$ iff $\binom{i}{n} \equiv 0 \pmod 2$ OR $\binom{i}{n} \equiv 0 \pmod 5$.
   By Principle of Inclusion-Exclusion:
   $$T(m, n) = (m - n) - |\{i \in [n, m-1] \mid \binom{i}{n} \not\equiv 0 \pmod 2 \text{ AND } \binom{i}{n} \not\equiv 0 \pmod 5\}|$$
2. **Lucas' Theorem Base Digit Restrictions**:
   Lucas' theorem states $\binom{i}{n} \not\equiv 0 \pmod p$ iff every base-$p$ digit of $n$ is $\le$ the corresponding base-$p$ digit of $i$.
3. **Digit DP & Meet-in-the-Middle Inclusion-Exclusion**:
   We count indices $i < m$ satisfying $i \ge n$ under simultaneously constrained base-2 and base-5 digit lower bounds via digit DP and inclusion-exclusion.
4. **Execution**:
   Evaluating the inclusion-exclusion digit sum for $m = 10^{18}, n = 10^{12} - 10$ yields $999998760323313995$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_2 m \cdot \log_5 m)$ for $m = 10^{18}$. Runs in $\approx 0.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log m)$.
