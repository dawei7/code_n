# Reflexive Position - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{13} f(3^k)$, where $f(n)$ is the 1-based starting position of the $n$-th occurrence of integer $n$ as a substring in the infinite Champernowne constant string $S = 123456789101112131415\dots$.

### Champernowne Substring Boundary Decomposition:
1. **Occurrence Types**:
   Occurrences of $T = \text{str}(n)$ in $S$ occur in 3 topological configurations:
   - Type 1: $T$ is fully contained within a single integer $X$ concatenated in $S$.
   - Type 2: $T$ spans across two adjacent integers $X$ and $X+1$.
   - Type 3: $T$ spans across three adjacent integers $X, X+1, X+2$.
2. **Sequential Occurrence Counting**:
   For each target $n = 3^k$ ($k = 1 \dots 13$), we enumerate candidate numbers $X$ that produce $T$ as a substring, ordered by their starting position in $S$, until the $n$-th occurrence is reached.
3. **Execution**:
   Evaluating $f(3^k)$ for $k = 1 \dots 13$ and summing the values yields $1817442159593978$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K \cdot 3^K)$ for $K = 13$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log(3^K))$.
