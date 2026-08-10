## General

The adjacency matrix already stores, row by row, every fact needed to compute a vertex's degree. Row $i$ describes vertex $i$'s relationship with every possible vertex $j$:

$$
\texttt{matrix}[i][j]
=
\begin{cases}
1,&\text{if edge }\{i,j\}\text{ exists},\\
0,&\text{otherwise}.
\end{cases}
$$

Because each entry is binary, summing row $i$ counts exactly how many incident edges vertex $i$ has. The source implements that definition directly.

**Why one matrix row corresponds to one vertex**

The first index is the vertex whose neighbors are being described. For a fixed $i$, moving across columns $j=0,1,\ldots,N-1$ asks whether vertex $i$ connects to each possible endpoint $j$.

The degree of $i$ is

$$
\deg(i)=\sum_{j=0}^{N-1}\texttt{matrix}[i][j].
$$

There is no need to interpret a 1 as anything more complicated than one incident edge. A zero adds nothing.

The diagonal guarantee `matrix[i][i] = 0` means no row includes a self-loop. This matters because conventions for self-loops can count two toward an undirected degree, while a plain row sum would count a diagonal 1 only once. The simple-graph contract removes that ambiguity.

**How the nested loops realize the formula**

The source first creates `ans` with one zero for every row:

```text
ans = [0] * len(matrix)
```

During `for i, row in enumerate(matrix)`, `i` is both the row index and the vertex label. The inner loop visits each binary entry `x` in that row and performs

```text
ans[i] += x
```

After the first $t$ entries of row $i$ have been processed, `ans[i]` equals their sum. Processing the next entry adds one exactly when the next neighbor exists. At the end of the row, all $N$ potential neighbors have been considered, so `ans[i]` equals $\deg(i)$.

Each row has its own accumulator position. Finishing one row does not affect any other answer entry.

**Why matrix symmetry does not cause an error**

For an undirected edge $\{i,j\}$, the symmetric matrix contains

$$
\texttt{matrix}[i][j]=1
\quad\text{and}\quad
\texttt{matrix}[j][i]=1.
$$

The algorithm visits both entries. That does not double-count the degree of one vertex. The first entry contributes one to `ans[i]`, while the symmetric entry contributes one to `ans[j]`. An undirected edge is incident to both endpoints, so both degrees must increase.

Double-counting would be a concern if the task asked for the total number of edges. In that different task, summing the entire matrix would count each undirected edge twice. Here the output deliberately asks for a separate incident-edge count at every endpoint.

**A complete example**

For

```text
matrix = [[0, 1, 1],
          [1, 0, 1],
          [1, 1, 0]]
```

the row sums are:

$$
0+1+1=2,
$$

$$
1+0+1=2,
$$

and

$$
1+1+0=2.
$$

The method returns `[2, 2, 2]`. Although the whole matrix contains six ones, the graph has three undirected edges; each of those edges correctly contributes to two different vertex degrees.

For an isolated vertex, its row contains only zeros. Its accumulator never changes from the initial zero, so the returned degree is zero.

**Why every returned value is exact**

Fix a vertex $i$. Every edge incident to $i$ has one other endpoint $j$ and therefore produces one matrix entry `matrix[i][j] = 1`. The inner loop includes that one in `ans[i]`, so no incident edge is missed.

Conversely, every one added from row $i$ denotes an edge between $i$ and its column vertex. Therefore the loop never adds a non-incident edge. The row sum has a one-to-one correspondence with the edges connected to $i$.

Applying the same argument independently to every row proves that the returned array has the required degree at every index.

## Complexity detail

Let $N$ be the number of vertices. An adjacency matrix has exactly $N^2$ entries. The nested loops inspect every entry once and perform constant work for it, so the running time is

$$
O(N^2).
$$

This cost is unavoidable for a general matrix input if the algorithm must distinguish inputs that may differ at any position. Even though symmetry means half the entries repeat graph information, reading each row directly is the simplest way to produce all row sums. A triangular scan could update both endpoints from one half of the matrix, but it would still inspect $\Theta(N^2)$ possible positions.

The returned `ans` list contains $N$ integers, so it uses

$$
O(N)
$$

space. Apart from this required output, the working variables `i`, `row`, and `x` use $O(1)$ auxiliary space. If output storage is excluded from the auxiliary-space convention, the extra working space is $O(1)$; the manifest's $O(N)$ bound includes the returned array.

The input matrix is read but never modified.

## Alternatives and edge cases

- **Built-in row sums:** Returning `[sum(row) for row in matrix]` expresses the same algorithm more compactly, with the same $O(N^2)$ time and $O(N)$ output space.
- **Upper-triangle scan:** Visit only entries with $i<j$ and increment both endpoint degrees for every one. This uses symmetry explicitly but does not improve the asymptotic time for dense matrix storage.
- **Adjacency-list input:** If the graph were stored by neighbors, degrees could be obtained in $O(N+E)$ time. Converting this matrix first would still require reading $N^2$ entries.
- **Single vertex:** The sole diagonal entry is zero, so the answer is `[0]`.
- **Isolated vertex:** An all-zero row leaves its accumulator at zero.
- **Complete simple graph:** Every row has $N-1$ ones and one diagonal zero, so every returned degree is $N-1$.
- **Symmetric duplicate entries:** They belong to different vertex accumulators and correctly account for the edge at both endpoints.
- **Zero diagonal requirement:** The row-sum method relies on the promise of no self-loops; a different self-loop degree convention would need explicit handling.
- **Binary-entry requirement:** Summation works because 1 means one edge and 0 means none. Weighted adjacency values would produce weighted sums rather than ordinary degrees.
- **Input preservation:** The method does not sort or alter any row, so the supplied matrix remains unchanged.
