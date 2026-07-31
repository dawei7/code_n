## Function Contract

**Inputs**

- `edges`: The $n-1$ undirected edges of a tree rooted at node `0`.
- `nums`: The length-$n$ array of initial node values.
- `k`: The minimum permitted edge distance between every pair of inverted nodes.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum total of the final node values over every inversion-node subset whose distinct members are pairwise at distance at least `k`.
