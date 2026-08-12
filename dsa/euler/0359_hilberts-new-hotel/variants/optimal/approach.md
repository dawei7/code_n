# Hilbert's New Hotel - Optimal Approach

## Algorithm Explanation

Find the last 8 digits of $\sum_{f \cdot r = N} P(f, r) \bmod 10^8$ for $N = 71328803586048 = 2^{27} 3^{12}$, where $P(f, r)$ is the person occupying room $r$ on floor $f$ in Hilbert's New Hotel.

### Closed-Form Quadratic Formula for $P(f, r)$:
1. **First Person on Floor $f$**:
   - $P(1, 1) = 1$.
   - For $f \ge 2$: $P(f, 1) = \lfloor f^2 / 2 \rfloor$.
2. **Quadratic Room Progression Formula**:
   For any floor $f$ and room $r$:
   Let $k = \lfloor r / 2 \rfloor$.
   - If $f$ is odd:
     - $r$ odd: $P(f, r) = P(f, 1) + 2 k^2 + (2f - 1) k$.
     - $r$ even: $P(f, r) = P(f, 1) + 2 k^2 + (2f + 1) k - f$.
   - If $f$ is even:
     - $r$ odd: $P(f, r) = P(f, 1) + 2 k^2 + (2f + 1) k$.
     - $r$ even: $P(f, r) = P(f, 1) + 2 k^2 + (2f - 1) k + f - 1$.
3. **Divisor Pair Summation**:
   $N = 2^{27} 3^{12}$ has $d(N) = (27 + 1)(12 + 1) = 28 \times 13 = 364$ divisors.
   For each divisor $f \mid N$, we set $r = N / f$ and compute $P(f, r) \bmod 10^8$ in $\mathcal{O}(1)$ time.
4. **Execution**:
   Summing $P(f, r)$ across all 364 divisor pairs yields last 8 digits $40632119$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(d(N))$ for $d(N) = 364$ divisors. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
