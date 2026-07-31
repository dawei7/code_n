## General

**The closest path vertex is the median of three tree nodes**

For a query `(start, end, node)`, the desired vertex is where the route from
`node` first joins the unique path from `start` to `end`. This vertex lies on
all three pairwise paths among the query nodes and is their tree median. Moving
away from it along the `start`-to-`end` path only increases the distance from
`node`, so the median is exactly the closest path vertex.

**Recover the median from three lowest common ancestors**

Root the tree at node 0. Compute
`lca(start, end)`, `lca(start, node)`, and `lca(end, node)`. The tree median is
the deepest of these three vertices.

To see why, consider the three rooted paths from the query nodes toward the
root. Two of the nodes share their deepest common branch up to the median,
while the third joins no lower. The corresponding pairwise LCA is the median;
the other pairwise LCAs are either the same vertex or ancestors of it.
Therefore selecting the candidate with maximum depth returns the unique common
meeting point and hence the desired projection.

**Answer LCAs with binary lifting**

An iterative traversal records every node's depth and immediate parent. Build
`parent[k][v]`, the $2^k$-th ancestor of `v`. To find an LCA, first lift the
deeper node until both depths match, then lift both nodes together from the
largest power of two downward until their parents agree.

Each query performs exactly three LCA computations and chooses their deepest
result.

## Complexity detail

Let $m=\lvert\texttt{query}\rvert$. Building the adjacency list and depths
takes $O(n)$ time. The binary-lifting table takes $O(n\log n)$ time and space.
Each of the $m$ queries performs three $O(\log n)$ LCA operations, so total
time is $O((n+m)\log n)$ and auxiliary space is $O(n\log n)$.

## Alternatives and edge cases

- **Reconstruct the requested path per query:** Breadth-first search can find the path and then its closest vertex, but costs $O(nm)$ total time.
- **All-pairs distances:** Precomputing every tree distance makes each query easy but uses $O(n^2)$ time and space.
- **Euler tour plus range-minimum queries:** This also supports fast LCAs, with different preprocessing and implementation tradeoffs.
- **`start == end`:** The path contains one node, which is necessarily the answer.
- **Query node lies on the path:** Its distance is zero, so it is returned.
- **Query node equals an endpoint:** That endpoint is the answer.
- **Reversed endpoints:** The undirected path and answer do not change.
- **Single-node tree:** Every valid query returns node 0.
- **Root dependence:** Individual LCAs depend on the chosen root, but their deepest candidate still represents the root-independent tree median.
