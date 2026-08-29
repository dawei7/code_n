## General

Treat each person as a graph vertex and each dislike pair as an undirected edge. The two people at the endpoints of every edge must be placed in different groups. The requested split exists exactly when this graph is bipartite, meaning its vertices can be colored with two colors so every edge connects different colors.

The solution first converts labels 1 through `n` to zero-based indices 0 through `n - 1`. Each dislike is inserted in both adjacency lists because the restriction is mutual for grouping purposes: if `a` and `b` cannot share a group, each must be seen as a neighbor of the other during traversal.

The `color` array uses three values:

- 0 means the person has not been assigned.
- 1 means the first group.
- 2 means the second group.

The helper `dfs(i, c)` assigns color `c` to vertex `i` and explores all of its neighbors.

**Check every edge from the current vertex.** For a neighbor `j`:

- If `color[j] == c`, both endpoints would be in the same group, so the coloring is invalid and DFS returns false.
- If `color[j] == 0`, the neighbor is uncolored and must receive the opposite color. Because valid colors are 1 and 2, `3 - c` toggles them: $3-1=2$ and $3-2=1$.
- If the neighbor is already colored with the opposite color, that edge is already satisfied and no recursive call is necessary.

Any recursive failure propagates immediately to the original call.

**Why coloring captures the partition.** If DFS succeeds, place every color-1 person in one group and every color-2 person in the other. Every dislike edge was checked from its endpoints and has different colors, so the split satisfies all restrictions. Unconnected people may receive either color without harm.

Conversely, suppose a valid two-group split exists. Assign color 1 to the first group and color 2 to the second. Every dislike edge crosses groups, so no same-color conflict exists. DFS's forced opposite-color assignments are consistent within each connected component up to swapping both color names. Therefore it cannot report a conflict for a genuinely bipartite graph.

An odd cycle explains failure. Alternating colors around a triangle assigns colors 1, 2, then 1 to its first three traversal positions, but the closing edge connects two color-1 vertices. No two groups can satisfy all three dislike pairs. Even cycles alternate consistently and cause no conflict.

**Disconnected components must each be started.** A DFS from person zero may not reach everyone. The final expression iterates over every color entry:

```text
all(c or dfs(i, 1) for i, c in enumerate(color))
```

When the enumerated value `c` is already 1 or 2, it is truthy, so that vertex belongs to a component already checked and DFS is skipped. When `c` is zero, the expression starts a new component with color 1. Choosing color 1 is arbitrary; swapping colors across an entire disconnected component changes no validity.

Python's `all` stops at the first false value. Thus any conflicting component returns false immediately. If every existing or newly explored component produces a truthy value, all components are bipartite and the result is true.
Along every traversal-tree edge, an uncolored neighbor receives the opposite color. For an edge to a previously colored vertex, the explicit equality test verifies compatibility. Therefore success means every examined edge is bichromatic. All vertices and adjacency entries in the component are eventually reached, so every component edge is examined. A conflict proves two parity paths demand incompatible colors, which is exactly the obstruction to bipartition.

## Complexity detail

Let $n$ be the number of people and $m$ the number of dislike pairs. Building the undirected adjacency list stores two entries per pair. Across all DFS calls, every vertex is colored once and every adjacency entry is inspected once.

- **Time complexity:** $O(n+m)$.
- **Space complexity:** $O(n+m)$ for the adjacency list, color array, and recursion stack in the worst case.

The recursion depth can reach $O(n)$ for a long path. With the allowed $n=2000$, a sufficiently deep component may exceed Python's default recursion limit in some environments; an iterative stack or queue would preserve the same algorithm and asymptotic bounds more robustly.

## Alternatives and edge cases

- **Breadth-first coloring:** A queue can assign alternating colors level by level. It has the same $O(n+m)$ bounds and avoids recursion-depth concerns.
- **Union-find:** For each person, union all disliked neighbors into the opposite side and detect contradictions. This works but is less direct than two-color traversal.
- **Try all two-group assignments:** There are $2^n$ assignments, while graph coloring resolves forced choices in linear time.
- **Check only one connected component:** This can miss an odd cycle elsewhere. The outer `all(...)` must cover every uncolored vertex.
- **No dislikes:** Every vertex begins a trivial component or is harmlessly colored; any partition works and the result is true.
- **Isolated people:** They can join either group. Starting them with color 1 creates no edge conflict.
- **One dislike pair:** Its endpoints receive opposite colors and the result is true.
- **Odd cycle:** Alternation returns to the start with the wrong color and correctly produces false.
- **Even cycle:** Alternation closes consistently and is valid.
- **Repeated traversal edges:** The undirected edge appears in both adjacency lists, but already colored opposite endpoints pass the check without recursion.
- **Any group size:** Neither group is required to be nonempty or balanced. Color counts do not enter the decision.
- **One-based input labels:** Subtracting one before adjacency construction is required because `color` uses zero-based indexing.
- **Unique pairs:** The contract prevents duplicate dislikes, though duplicates would not change coloring correctness.
- **Deep graph:** Iterative BFS or DFS is preferable if the runtime's recursion limit is below the maximum component depth.
