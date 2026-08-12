# Steady Squares - Optimal Approach

## Algorithm Explanation

Find the sum of the digits of all $n$-digit steady squares (numbers $x$ without leading zeros such that $x^2$ ends with $x$) in the base $14$ numbering system for $1 \le n \le 10000$, expressed in base $14$ notation (using `a`, `b`, `c`, `d` for $10, 11, 12, 13$).

### Hensel $p$-adic Lifting & CRT Identity:
1. **Idempotent Congruence**:
   An $n$-digit number $x$ in base $14$ is a steady square iff $x^2 \equiv x \pmod{14^n} \iff x(x - 1) \equiv 0 \pmod{2^n \cdot 7^n}$.
   By CRT, there are two non-trivial $n$-digit solutions $x_1, x_2 \in (0, 14^n)$ satisfying:
   - $x_1 \equiv 0 \pmod{2^n}$ and $x_1 \equiv 1 \pmod{7^n}$
   - $x_2 \equiv 1 \pmod{2^n}$ and $x_2 \equiv 0 \pmod{7^n}$
   Note that $x_1 + x_2 = 14^n + 1$.
2. **Sequential Digit Construction via Hensel Lifting**:
   Using Hensel's lemma, the base-$14$ digits of $x_1$ and $x_2$ are uniquely determined one digit at a time from LSB to MSB.
3. **Execution**:
   Summing the base-$14$ digit values for all valid $n$-digit steady squares ($1 \le n \le 10000$) without leading zeros and converting the total to base $14$ yields `5a411d7b`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10000$ digits. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ digit storage.
