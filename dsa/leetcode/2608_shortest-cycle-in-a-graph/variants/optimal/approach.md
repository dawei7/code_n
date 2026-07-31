## General

Build an undirected adjacency list. For each vertex `start`, run breadth-first search while recording every discovered vertex's distance from `start` and its parent in the BFS tree.

When an edge `(u, v)` reaches an undiscovered vertex, it becomes a tree edge and sets that vertex's distance. When both endpoints have already been discovered and neither is the other's parent through the examined direction, the edge is not the tree edge that led back toward the root. The two BFS-tree paths from `start` to $u$ and $v$, together with edge `(u,v)`, contain a cycle of length

$$
\texttt{distance[u]}+\texttt{distance[v]}+1.
$$

The paths may share a prefix, but running BFS from every possible start ensures that a shortest cycle is measured from a vertex on that cycle with the appropriate shortest-path branches. In particular, choose any vertex of a globally shortest cycle as the BFS root. The first non-tree connection completing that cycle reports no length larger than the cycle, while no reported closed walk can imply a simple cycle shorter than the global optimum.

Keep the minimum candidate from every BFS. If no non-tree edge is encountered, every component is acyclic and the answer is $-1$.

## Complexity detail

Let $n$ be the number of vertices and $m$ the number of edges. One BFS takes $O(n+m)$ time, and it is started from each of the $n$ vertices, giving $O(n(n+m))$ total time.

The adjacency lists use $O(n+m)$ space. Each BFS also uses $O(n)$ distance, parent, and queue storage, so the total auxiliary-space bound remains $O(n+m)$.

## Alternatives and edge cases

- **Remove each edge and search between its endpoints:** This is correct because a cycle containing that edge exists exactly when its endpoints remain connected, but it costs $O(m(n+m))$ time and is slower on dense graphs.
- **Depth-first search alone:** DFS detects whether a cycle exists, but ordinary discovery depths do not guarantee the shortest cycle length.
- **Disconnected graph:** Every BFS stays inside one component, and the global minimum naturally spans all components.
- **Forest:** No edge connects two already discovered vertices except a parent edge, so the result remains $-1$.
- **Triangle:** Three is the smallest possible cycle length because the graph has no self-loops or parallel edges.
- **Shared vertices and edges:** Overlapping cycles are handled independently through their non-tree edges; only the smallest reported length matters.
