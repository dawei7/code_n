# Minkowski Sums - Optimal Approach

## Algorithm Explanation

Find the number of sides of the Minkowski sum $S_{1864} + S_{1865} + \dots + S_{1909}$, where $S_n$ is the regular filled $n$-sided polygon.

### Minkowski Edge Merger & Farey Fraction Inclusion:
1. **Minkowski Edge Property**:
   The Minkowski sum of convex polygons has edges corresponding to all unique edge directions (normal angles) among the constituent shapes. Parallel edges merge into a single combined edge.
2. **Normal Angle Equivalence**:
   For $S_n$, the normal angle of each edge corresponds to the fraction $\frac{k}{n} \times 2\pi$ for $k \in \{1, 2, \dots, n\}$.
   Therefore, the total number of sides is the count of distinct reduced fractions $\frac{p}{q}$ with $\gcd(p, q) = 1$ present in $\bigcup_{n=a}^b F_n$.
3. **Multiple Criterion & Euler's Totient**:
   A denominator $q$ appears in $\bigcup_{n=a}^b F_n$ if and only if $q$ has at least one multiple in $[a, b]$, i.e. $\lfloor b / q \rfloor > \lfloor (a - 1) / q \rfloor$.
   For each such $q$, there are exactly $\phi(q)$ coprime numerators $p \in [1, q]$.
4. **Execution**:
   Summing $\phi(q)$ for all $q \in [1, 1909]$ satisfying the interval multiple condition yields $86226$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(b \sqrt{b})$ for $b = 1909$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
