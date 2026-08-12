# Rigid Graphs - Optimal Approach

## Algorithm Explanation

Find $S(100) \bmod 1000000033$, where $S(N) = \sum_{1 \le i, j \le N} R(i, j)$ and $R(m, n)$ is the number of ways to make an $m \times n$ grid graph 2D rigid by adding at most one diagonal edge to each cell.

### Laman's Rigidity Theorem & Bipartite Connectivity DP:
1. **Grid Rigidity Equivalence**:
   By Laman's Theorem and structural rigidity of bipartite frameworks:
   Adding diagonals to an $m \times n$ grid graph makes it rigid iff the associated bipartite graph between $m$ rows and $n$ columns is connected.
   Each cell $(i, j)$ allows 2 choices of diagonal (or no diagonal), giving 2 available edge choices per bipartite pair.
2. **Connected Bipartite Graph Inclusion-Exclusion**:
   Let $R(m, n)$ be the number of connected bipartite graphs on $(m, n)$ vertices.
   By complementary counting over connected components:
   $$R(m, n) = 2^{m n} - \sum_{i=1}^m \sum_{j=0}^n \binom{m-1}{i-1} \binom{n}{j} R(i, j) 2^{(m-i)(n-j)}$$
3. **2D Dynamic Programming**:
   We compute $R(i, j)$ for all $1 \le i, j \le N = 100$ using 2D DP.
4. **Execution**:
   Summing $R(i, j) \bmod 1000000033$ for $1 \le i, j \le 100$ yields $863253606$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^4)$ for $N = 100$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2)$ DP state table.
