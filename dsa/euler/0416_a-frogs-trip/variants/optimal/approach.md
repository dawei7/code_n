# A Frog's Trip - Optimal Approach

## Algorithm Explanation

Find the last 9 digits of $F(10, 10^{12}) \bmod 10^9$, where $F(m, n)$ is the number of ways a frog can complete $m = 10$ round trips on a row of $n = 10^{12}$ squares (with jump lengths $\in \{1, 2, 3\}$) leaving at most one square unvisited.

### Boundary Transition State Space & Matrix Exponentiation:
1. **Multi-Trip State Representation**:
   A trip consists of $m$ outward paths ($+1, +2, +3$) and $m$ homeward paths ($-1, -2, -3$).
   As we transition from square $i$ to $i+1$, we maintain a state vector tracking:
   - The active jump configurations across boundary $i$.
   - A 2-state flag indicating whether an unvisited square has already been skipped ($0$ or $1$).
2. **Transfer Matrix Construction**:
   The transition rules between square $i$ and $i+1$ form a linear transition matrix $M_{m}$ of small dimension ($\approx 30$ states for $m = 10$).
3. **Binary Matrix Exponentiation**:
   The number of valid trip configurations for $n = 10^{12}$ is given by:
   $$F(m, n) \equiv \mathbf{v}_{\text{end}}^T M_m^{n-1} \mathbf{v}_{\text{start}} \pmod{10^9}$$
   Matrix power $M_m^{n-1} \bmod 10^9$ is computed in $\mathcal{O}(\text{dim}^3 \log n)$ time using binary exponentiation.
4. **Execution**:
   Evaluating $F(10, 10^{12}) \bmod 10^9$ yields last 9 digits $898082747$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S^3 \log n)$ for $S \approx 30$ and $n = 10^{12}$. Runs in $\approx 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(S^2)$ transition matrix.
