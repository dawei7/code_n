## General

Fix a candidate factor $D$. Any two points at Manhattan distance less than $D$ are forbidden from sharing a group; otherwise that pair would make the intra-group minimum smaller than $D$. Create a graph whose vertices are points and whose edges join exactly these too-close pairs. Assigning the points to two groups with factor at least $D$ is equivalent to coloring every graph edge with opposite endpoint colors, so $D$ is feasible exactly when this graph is bipartite.

**Introduce restrictions by distance.** Build every unordered point pair, label it with its Manhattan distance, and sort the edges. Process them from shortest to longest. A parity disjoint-set union structure records the requirement that each processed edge's endpoints have opposite colors. For every vertex, its parity bit describes its color difference from the representative of its component.

When an edge joins different components, merge them with the representative parity chosen so its endpoints become opposite. When both endpoints already have the same representative, their existing parity relation is fixed. The new restriction is consistent if their parities differ; equal parities create an odd cycle and make the processed graph non-bipartite.

Suppose the first contradiction occurs while processing distance $d$. Before any distance-$d$ restriction was needed, all edges shorter than $d$ were bipartite, so a split with factor at least $d$ exists. Once the contradictory distance-$d$ edges are included, every threshold greater than $d$ is impossible. Thus $d$ is exactly the maximum partition factor. Equal-distance edges may be processed in any order: a contradiction anywhere in that batch still has threshold $d$. For `n = 2`, return the separately defined value `0`.

## Complexity detail

Let $n=\lvert\texttt{points}\rvert$ and $m=n(n-1)/2$. Constructing the $m$ weighted pairs takes $O(n^2)$ time, and sorting them takes $O(n^2\log n)$ time. Parity-DSU operations add $O(n^2\alpha(n))$ time, where $\alpha$ is the inverse Ackermann function, so sorting dominates. The edge list uses $O(n^2)$ space; DSU arrays use $O(n)$ additional space.

## Alternatives and edge cases

- **Binary search plus graph coloring:** Testing a distance threshold with BFS or DFS is valid. Binary-searching the sorted distinct distances also takes $O(n^2\log n)$ time, but repeatedly rebuilds or scans the too-close graph.
- **Enumerate all partitions:** Trying every two-color assignment and measuring its intra-group pairs takes exponential time, up to $O(2^n n^2)$.
- **Ordinary DSU without parity:** Connectivity alone cannot represent the requirement that edge endpoints have different colors; the color difference must be tracked.
- **Exactly two groups:** A bipartite coloring supplies the two assignments. For $n\ge3$, the complete pair graph eventually creates an odd cycle, so a contradiction distance exists.
- **Duplicate coordinates:** Their distance is `0`; parity constraints still handle them, and the optimal factor may be zero.
- **Singleton group:** It contributes no pair, so for three points the farthest pair can share one group while the remaining point stands alone.
- **Two points:** Both groups are forced to be singletons, and the source explicitly defines the answer as `0`.
