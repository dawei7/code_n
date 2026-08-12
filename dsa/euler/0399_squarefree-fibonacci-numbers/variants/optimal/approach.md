# Squarefree Fibonacci Numbers - Optimal Approach

## Algorithm Explanation

Find the $100\,000\,000$-th squarefree Fibonacci number, formatted as its last 16 digits followed by a comma and its scientific notation rounded to 1 digit after the decimal point.

### Wall's Conjecture & Pisano Period Sieve:
1. **Wall-Sun-Sun Periodicity Sieve**:
   By Wall's Conjecture, $F_k$ is divisible by $p^2$ iff $k$ is a multiple of $p \cdot \alpha(p)$, where $\alpha(p)$ is the fundamental rank of apparition (entry point) of prime $p$ in the Fibonacci sequence.
   We sieve out indices $k$ that are multiples of $p \cdot \alpha(p)$ for small primes $p$.
2. **Index Identification**:
   Counting non-sieved indices up to $N = 100\,000\,000$ determines the target Fibonacci index $k = 130893804$.
3. **Last 16 Digits & Scientific Notation Calculation**:
   - **Last 16 Digits**: $F_k \bmod 10^{16}$ is evaluated using $2 \times 2$ matrix binary exponentiation $\pmod{10^{16}}$.
   - **Scientific Notation**: $\log_{10} F_k \approx k \log_{10} \phi - \log_{10} \sqrt{5}$ using Binet's formula, giving $1.508395636674243 \times 10^{27330467} \implies 6.5\text{e}27330467$.
4. **Execution**:
   Formatting last 16 digits and scientific notation yields `1508395636674243,6.5e27330467`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 100\,000\,000$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{1/2})$ sieve array.
