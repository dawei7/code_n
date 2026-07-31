## General

**A row lists every possible neighbor of one vertex**

Fix a vertex $i$. Column $j$ of row $i$ is $1$ exactly when the edge $\{i,j\}$ exists. Because every possible neighbor has one column, summing row $i$ counts all edges incident to $i$. The diagonal entry is guaranteed to be zero, so no self-loop can add a spurious contribution.

Process the rows in vertex-label order. Sum the binary entries in each row and append that total to the result. Symmetry means an undirected edge appears once in each endpoint's row, which is precisely what the requested degree array needs: the edge contributes one to each endpoint, not twice to either endpoint.

For every vertex $i$, the algorithm returns $\sum_{j=0}^{N-1}\texttt{matrix[i][j]}$. By the adjacency-matrix definition, that sum is exactly the number of vertices joined to $i$, hence exactly its degree. Applying the same argument independently to every row proves that the complete returned array is correct.

## Complexity detail

There are $N^2$ matrix entries, and each is included in one row sum, so the running time is $O(N^2)$. The returned degree array uses $O(N)$ space; beyond that required output, the scan uses $O(1)$ auxiliary state.

The `asymptotic_optimality` certificate replaces runtime scaling. A simple undirected graph has $N(N-1)/2=\Theta(N^2)$ independently selectable edge indicators in the upper triangle. Changing any one of them changes two required degrees, so an exact algorithm must determine all of them in the worst case. The accepted $O(N^2)$ scan therefore matches the $\Omega(N^2)$ problem-level lower bound, with no genuine principal slower strategy that would justify artificial benchmark tiers.

## Alternatives and edge cases

- **Upper-triangle accumulation:** Scan only entries with $i<j$ and increment both endpoint counts for every `1`. This also takes $O(N^2)$ time and uses the same $O(N)$ output storage.
- **Convert to adjacency lists:** Building lists before counting degrees still requires reading the entire supplied matrix and adds storage without improving the asymptotic time.
- **Isolated vertex:** A row of all zeros correctly produces degree $0$.
- **Complete graph:** Every row contains exactly $N-1$ ones because its diagonal entry is zero, so every degree is $N-1$.
- **Single vertex:** The only legal matrix is `[[0]]`, whose result is `[0]`.
- **Symmetric duplicate entries:** `matrix[i][j]` and `matrix[j][i]` describe the same edge but belong to different row sums, contributing once to each endpoint as required.
