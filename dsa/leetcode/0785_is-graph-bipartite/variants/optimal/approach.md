## General
**Propagate opposite colors**

Store `0` for an uncolored vertex and `1` or `-1` for the two groups. Choose an uncolored start vertex, assign one color, and breadth-first search its component. Every uncolored neighbor receives the opposite color of the current vertex.

**Detect an impossible constraint**

If an edge reaches a neighbor that already has the current vertex's color, the two-group requirement is contradictory, so return false. Otherwise every processed edge has opposite-colored endpoints.

**Cover disconnected components**

One search may not visit the whole graph. Start another search from each still-uncolored vertex; an isolated vertex simply forms a valid one-vertex component. If all components finish without conflict, the recorded colors themselves provide a valid bipartition. Conversely, a same-color edge arises only after the path constraints force both endpoints into one group, which makes any bipartition impossible.

## Complexity detail
Each of the `V` vertices enters the queue at most once, and each undirected edge is inspected from both endpoints, for $O(V + E)$ time. The color array and queue use $O(V)$ auxiliary space.

## Alternatives and edge cases
- **Depth-first coloring:** An iterative or recursive DFS applies the same opposite-color rule with $O(V + E)$ time.
- **Union-find neighbors:** Union all neighbors of a vertex into the opposite set while checking that the vertex is not connected to them; this is less direct but valid.
- **Adjacency-matrix scan:** Testing every possible neighbor for every visited vertex takes $O(V^2)$ time on sparse graphs.
- **Try every partition:** Enumerating all two-group assignments takes exponential time.
- **Disconnected graph:** Every component needs its own initial color.
- **Isolated vertices:** They can belong to either group and never cause a conflict.
- **Odd cycle:** Its alternating constraints return to the start with the wrong color, so the graph is not bipartite.
- **Even cycle or tree:** Alternating colors remain consistent throughout the component.
