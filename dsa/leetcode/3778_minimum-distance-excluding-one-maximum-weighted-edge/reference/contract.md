## Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: The graph's unique undirected edges, each encoded as `[u_i, v_i, w_i]`.

Let $N=n$ and $E=\lvert\texttt{edges}\rvert$. Each listed pair satisfies $u_i<v_i$; this ordering is part of the input representation and does not give the undirected edge a direction. A path's excluded edge is chosen from that path, not from the graph as a whole.

**Return value**

Return the least path-weight sum from node `0` to node `n - 1` after omitting exactly the first occurrence of that path's maximum edge weight.
