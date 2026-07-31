## Function Contract

**Inputs**

- `matrix`: A square, symmetric binary adjacency matrix for a simple undirected graph.

Let $N=\texttt{matrix.length}$. Vertex labels and both matrix indices range from $0$ through $N-1$. A zero diagonal means the graph has no self-loops.

**Return value**

Return an array of length $N$ whose entry at index $i$ is the number of edges connected to vertex $i$.
