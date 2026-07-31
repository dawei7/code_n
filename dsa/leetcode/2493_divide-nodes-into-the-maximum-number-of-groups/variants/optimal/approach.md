## General

**The edge rule first demands bipartiteness.** Group indices change by exactly one across every edge, so their parity alternates across the graph. An odd cycle would require its first node to have both parities and makes the assignment impossible. Traverse each connected component while assigning two colors; return `-1` as soon as an edge joins equal colors.

**A breadth-first level is a valid group index.** Fix a start node in a bipartite component and assign each node its shortest-path distance from that start, plus one. For adjacent nodes, shortest-path distances differ by at most one. Bipartiteness prevents equal distances because adjacent nodes have opposite distance parity, so their distances differ by exactly one. The BFS layers therefore give a valid grouping.

**The widest valid grouping is the diameter plus one.** If a component uses $k$ nonempty groups, choose nodes in its first and last groups. Every path between them changes the group index by only one per edge, so their distance is at least $k-1$. Thus $k$ cannot exceed the component diameter plus one. Conversely, BFS from one endpoint of a diameter creates exactly that many layers, so the bound is attainable.

Run BFS from every node in the component and retain the largest number of discovered levels. This finds the exact diameter without relying on the two-sweep shortcut, which is guaranteed for trees but not arbitrary graphs. Components have no connecting constraints, so their maximum layer counts can be placed in disjoint consecutive ranges and summed.

## Complexity detail

Let $m = \lvert\texttt{edges}\rvert$. Building the adjacency list and checking all components take $O(n+m)$ time. The all-source breadth-first searches each cost $O(n+m)$ in the worst case, for $O(n(n+m))$ total time. The adjacency list, colors, component lists, queue, and one distance array use $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Floyd-Warshall distances:** After a separate bipartiteness check, all-pairs shortest paths reveal each component diameter, but require $O(n^3)$ time and $O(n^2)$ space.
- **Two BFS sweeps per component:** This finds a tree diameter, but it is not a general exact-diameter algorithm for arbitrary bipartite graphs.
- **Union-Find:** It can identify connected components, but a graph traversal is still needed to test bipartiteness and measure BFS layers.
- **Odd cycle in any component:** One impossible component makes the required all-node partition impossible, so the answer is `-1`.
- **Disconnected components:** Their layer counts add; they must not be merged into one diameter calculation.
- **Isolated nodes:** Each isolated node is its own component and contributes one group even though the input contains at least one edge elsewhere.
- **Even cycles and cross edges:** They remain valid when bipartite, but may shorten distances and reduce the maximum layer count relative to a path with the same nodes.
