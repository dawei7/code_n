## General
**Store every undirected neighborhood**

Build a set of adjacent rooms for each room. Because corridors work in both directions, insert `v` into `neighbors[u]` and `u` into `neighbors[v]`. Set intersection can then identify common neighbors without scanning every room.

**Count the closing room for each corridor**

For a corridor `[u, v]`, every room in `neighbors[u] & neighbors[v]` has a corridor to both endpoints. That common neighbor closes one three-room cycle containing `[u, v]`. Conversely, every triangular cycle has exactly this form for each of its edges, so the intersection counts include all and only valid cycles.

**Correct the fixed triple counting**

A triangle on rooms `{a, b, c}` contributes `c` as a common neighbor of edge `[a, b]`, `b` for `[a, c]`, and `a` for `[b, c]`. It is therefore accumulated exactly three times, independent of traversal direction or starting room. Dividing the total shared-neighbor count by three gives the number of distinct room sets requested.

## Complexity detail
Building the neighborhood sets costs $O(n+E)$ time and space. Intersecting the smaller endpoint neighborhood for every corridor costs

$$
O\left(\sum_{[u,v]\in\texttt{corridors}}\min(d(u),d(v))\right).
$$

The standard degree-splitting bound makes this sum $O(E^{3/2})$, so total time is $O(n+E^{3/2})$. The adjacency sets contain $2E$ entries and use $O(n+E)$ space.

## Alternatives and edge cases
- **Enumerate every room triple:** Checking all $\binom{n}{3}$ triples with constant-time edge lookup is correct but costs $O(n^3)$ even for sparse mazes.
- **Linear adjacency searches:** Enumerating triples while scanning neighbor lists for each edge can degrade to $O(n^4)$ on dense graphs.
- **No cycle:** A tree, isolated corridor, or longer cycle without a chord contributes zero.
- **Shared edges:** Several triangles may use the same corridor; each distinct three-room set must still be counted.
- **Orientation and rotation:** Reversing a traversal or choosing another starting room describes the same unordered room triple.
- **Disconnected maze:** Count triangles independently in every connected component.
