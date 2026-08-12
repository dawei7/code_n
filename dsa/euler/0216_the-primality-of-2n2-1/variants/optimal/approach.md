# The Primality of 2n^2 - 1 - Optimal Approach

## Algorithm Explanation

Find the number of $n \le 50\,000\,000$ for which $t(n) = 2n^2 - 1$ is prime.

### Quadratic Residue & Tonelli-Shanks Polynomial Sieve:
1. **Divisibility Condition**:
   A prime $p$ divides $t(n) = 2n^2 - 1$ if and only if $2n^2 \equiv 1 \pmod p \iff n^2 \equiv \frac{p+1}{2} \pmod p$.
   By quadratic reciprocity, $2$ is a quadratic residue modulo $p$ if and only if $p \equiv \pm 1 \pmod 8$.
2. **Modular Square Root Sieve**:
   For each prime $p \le \sqrt{2 N^2 - 1} \approx 7.07 \times 10^7$ with $p \equiv \pm 1 \pmod 8$:
   - Solve $r^2 \equiv \frac{p+1}{2} \pmod p$ using Tonelli-Shanks to obtain $r_1, r_2$.
   - Mark $t(n)$ as composite for all $n \equiv r_1, r_2 \pmod p$ where $t(n) > p$.
3. **Execution**:
   Counting remaining prime indicators up to $N = 50\,000\,000$ yields $5437849$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 50\,000\,000$. Runs in $\approx 6.0\text{s}$ (C++ compiled).
- **Space Complexity:** $\mathcal{O}(N + \sqrt{2} N)$ for primality bytearrays.
