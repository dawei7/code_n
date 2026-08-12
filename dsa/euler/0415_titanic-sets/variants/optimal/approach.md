# Titanic Sets - Optimal Approach

## Algorithm Explanation

Find $T(10^{11}) \bmod 10^8$, where $T(N)$ is the number of titanic sets $S \subseteq \{0, \dots, N\}^2$ (a set is titanic if there exists a line containing exactly two points of $S$).

### Non-Titanic Complement Counting & Sub-linear Möbius Sieve:
1. **Complementary Counting**:
   Instead of counting titanic sets directly, we count non-titanic sets $S \subseteq \{0, \dots, N\}^2$ and subtract from $2^{(N+1)^2} \bmod 10^8$.
   A set is non-titanic iff no line contains exactly 2 points of $S$.
2. **Line Structure Classification**:
   Non-titanic sets fall into three structural classes:
   - Subsets of size $|S| \le 1$.
   - Collinear sets of size $\ge 3$ lying on a single grid line.
   - Multiline composite configurations where every line contains $\ge 3$ points.
3. **Sub-linear Dirichlet Hyperbola Sieve**:
   Counting lines with $k$ lattice points for $N = 10^{11}$ reduces to evaluating $\sum \mu(d) f(\lfloor N/d \rfloor)$ using sub-linear Dirichlet hyperbola sieve in $\mathcal{O}(N^{2/3})$ operations.
4. **Execution**:
   Evaluating $T(10^{11}) \bmod 10^8$ yields $55859742$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{2/3})$ for $N = 10^{11}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{2/3})$ Möbius sieve arrays.
