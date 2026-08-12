# Laserbeam - Optimal Approach

## Algorithm Explanation

Find the number of ways a laser beam entering vertex $C$ can bounce off $N = 12017639147$ reflective surfaces and exit through vertex $C$.

### Unfolded Triangular Grid & Inclusion-Exclusion:
1. **Unfolded Grid Geometry**:
   Unfolding the reflections of an equilateral triangle maps the ray trajectory to a straight line from $(0, 0)$ to a triangular lattice point $(x, y)$.
   The total number of surface reflections $N$ relates to $k = \frac{N + 3}{2}$ via $x + y = k$.
2. **Lattice Vertex Condition for $C$**:
   A ray hits vertex $C$ after $N$ bounces if and only if:
   - $x + y = k$
   - $\gcd(x, y) = 1 \iff \gcd(x, k) = 1$
   - $x \equiv 2k \pmod 3$
3. **Inclusion-Exclusion Counting**:
   Using prime factorization $k = p_1^{e_1} \cdots p_m^{e_m}$, we count $x \in (0, k)$ satisfying $x \equiv 2k \pmod 3$ and $\gcd(x, k) = 1$ via principle of inclusion-exclusion.
4. **Execution**:
   Evaluating for $N = 12017639147$ yields $1209002624$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{N} + 2^{\omega(N)})$ where $\omega(N)$ is the number of distinct prime factors of $k$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log N)$ for prime factor storage.
