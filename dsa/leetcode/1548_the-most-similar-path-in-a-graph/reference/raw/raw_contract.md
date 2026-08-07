## Function Contract

**Inputs**

- `n`: Number of cities ($2 \le n \le 100$).
- `roads`: List of undirected edges `[u, v]`.
- `names`: List of $n$ city names.
- `targetPath`: List of $m$ target names ($1 \le m \le 100$).

**Return value**

Return a list of $m$ city indices forming a valid walk on the graph with minimum edit distance against `targetPath`.
