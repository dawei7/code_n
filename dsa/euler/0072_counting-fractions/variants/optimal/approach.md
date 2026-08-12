# Counting Fractions - Optimal Approach

## Algorithm Explanation

Count the total number of reduced proper fractions $\frac{n}{d}$ ($n < d, \gcd(n, d) = 1$) for $d \le 1000000$.

### Totient Equivalence
For each denominator $d$, the count of valid numerators $n < d$ coprime to $d$ is given by Euler's totient function $\phi(d)$.
Thus, the total count of reduced proper fractions is:
$$\text{Total} = \sum_{d=2}^{1000000} \phi(d)$$

### Totient Sieve Algorithm:
1. Initialize `phi` array of size $N + 1$ with `phi[i] = i`.
2. For each prime $p \le N$ (`phi[p] == p`), multiply `phi[j]` by $(1 - \frac{1}{p})$ for all multiples $j = p, 2p, 3p \dots$.
3. Compute and return `sum(phi[2:])`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 1000000$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Totient array storage.
