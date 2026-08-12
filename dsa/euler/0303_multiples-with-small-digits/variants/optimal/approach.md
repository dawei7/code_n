# Multiples with Small Digits - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10000} \frac{f(n)}{n}$, where $f(n)$ is the least positive multiple of $n$ whose decimal representation contains only digits $\le 2$ (i.e. $\{0, 1, 2\}$).

### Breadth-First Search Modulo $n$:
1. **Shortest Multiple Search State Space**:
   For each integer $n \in [1, 10000]$, we construct the smallest positive multiple with digits $\{0, 1, 2\}$ by searching the remainder graph modulo $n$.
2. **BFS Queue & Parent Pointers**:
   - Initial states: $r = 1 \bmod n$ and $r = 2 \bmod n$.
   - Transitions: $r_{\text{next}} = (10 r + d) \bmod n$ for $d \in \{0, 1, 2\}$.
   - We store parent pointers `parent[r] = (prev_r, digit)` to reconstruct the exact digit string of $f(n)$ once $r = 0$ is reached.
3. **Execution**:
   Summing $\frac{f(n)}{n}$ for all $n \le 10000$ yields $1111981904675169$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot \text{states})$ for $N = 10000$. Runs in $\approx 9.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ parent state mapping.
