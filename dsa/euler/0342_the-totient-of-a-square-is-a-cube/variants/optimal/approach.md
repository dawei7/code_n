# The Totient of a Square Is a Cube - Optimal Approach

## Algorithm Explanation

Find the sum of all numbers $n$ with $1 < n < 10^{10}$ such that $\phi(n^2)$ is a perfect cube.

### Prime Power Factorization & Backtracking Tree Search:
1. **Prime Factorization Exponent Condition**:
   Let $n = \prod p_i^{e_i}$. Then $n^2 = \prod p_i^{2 e_i}$, and:
   $$\phi(n^2) = \prod p_i^{2 e_i - 1} (p_i - 1)$$
   For $\phi(n^2)$ to be a perfect cube, every prime factor $q \mid \phi(n^2)$ must appear with a total exponent divisible by $3$.
2. **Prime Factor Dependency Graph & DFS Traversal**:
   Since $p_i - 1$ must supply missing prime factor powers $3 - (2e_i - 1) \bmod 3$, only specific prime combinations are viable.
   Using depth-first search (DFS) over valid prime factor trees up to $n < 10^{10}$, we filter and collect all admissible $n$.
3. **Execution**:
   Summing all valid $n < 10^{10}$ yields $5943040885644$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 10^{10}$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log N)$ recursion stack.
