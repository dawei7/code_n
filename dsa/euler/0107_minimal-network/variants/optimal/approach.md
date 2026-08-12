# Minimal Network - Optimal Approach

## Algorithm Explanation

Find the maximum weight saving achieved by removing redundant edges from a 40-vertex connected undirected network in `network.txt` while maintaining total connectivity.

### Kruskal's Minimum Spanning Tree (MST) Algorithm:
Removing the maximum total edge weight while keeping the graph connected is equivalent to finding the Minimum Spanning Tree (MST):
$$\text{Max Saving} = \sum_{e \in E} w(e) - w(\text{MST})$$

1. Parse the $40 \times 40$ adjacency matrix from `network.txt`.
2. Extract all unique undirected edges $e = (u, v)$ with weight $w(e)$ for $u < v$.
3. Sort all edges by weight in ascending order.
4. Apply **Kruskal's Algorithm** with **Disjoint Set Union (DSU)** with path compression:
   - Iterate sorted edges and add edge $e = (u, v)$ to MST if $u$ and $v$ belong to different connected components.
   - Stop when $|V| - 1 = 39$ edges have been added.
5. Return $\text{Total Weight} - w(\text{MST})$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(E \log E)$ where $V = 40, E \le 780$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(V + E)$ - DSU parent array and edge list.
