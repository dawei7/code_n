## Function Contract

**Inputs**

- `n`: The number of nodes in the tree ($1 \le n \le 1000$).
- `edges`: A list of $n-1$ pairs `[u, v]` representing undirected tree edges.
- `query`: A list of queries `[start, end, node]`, where $1 \le \text{query.length} \le 1000$.

**Return value**

Return a list of integers of length $\text{query.length}$, where the $i$-th element is the node on the simple path between `start` and `end` closest to `node` for query $i$.
