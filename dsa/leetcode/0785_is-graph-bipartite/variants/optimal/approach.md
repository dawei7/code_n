## General

**Translate the partition into a two-coloring**

A bipartite graph can split its vertices into sets `A` and `B` so every edge crosses between the sets. Assign color `1` to vertices in one set and color `-1` to vertices in the other.

Then the requirement becomes simple: every edge must connect vertices with opposite colors. The actual names or signs of the colors do not matter; only equality versus opposition matters.

The solution stores one integer per vertex in `color`:

- `0` means the vertex has not been colored;
- `1` means the first side;
- `-1` means the second side.

Using `-c` produces the opposite side without a conditional expression.

**Propagate forced colors with depth-first search**

Function `dfs(a, c)` assigns color `c` to vertex `a`. Once `a` has a side, every neighbor `b` is forced to use `-c`.

For each neighbor, the condition handles two failure routes:

`color[b] == c or (color[b] == 0 and not dfs(b, -c))`.

The first route detects an immediate conflict: `a` and `b` are joined by an edge but already have the same color.

The second route applies only to an uncolored neighbor. It recursively colors that neighbor oppositely and explores everything forced by that choice. If the recursive component exploration finds any conflict, it returns `False`, which propagates through every active call.

If a neighbor is already colored `-c`, neither route applies. That edge is consistent, so scanning continues.

**Why greedy coloring does not require backtracking**

Choosing the starting vertex's color may seem arbitrary, but swapping all colors within a connected component produces an equivalent partition. Once that first choice is made, every path forces the color of its endpoint according to whether the path length is even or odd.

There is therefore no meaningful alternative color choice to try at an individual neighbor. Giving a neighbor the same color would violate their connecting edge immediately. Giving it the opposite color is forced.

If two different paths later force contradictory colors for one vertex, the graph contains an odd cycle, and no global recoloring can resolve it. Returning false is conclusive; backtracking to flip only part of the component would break an edge elsewhere.

**Why an odd cycle creates a conflict**

Moving across an edge flips color. After an even number of edges, a path returns to the starting color; after an odd number, it expects the opposite color.

On an odd cycle, following all cycle edges returns to the starting vertex after an odd number of flips, requiring that vertex to be both colors. DFS observes this contradiction as an edge whose two endpoints have the same stored color.

Conversely, if the entire graph can be colored without such a conflict, vertices colored `1` form one independent set and vertices colored `-1` form the other. Every scanned edge crosses between them, which is exactly a bipartition.

**Handle disconnected components**

A single DFS reaches only vertices connected to its starting point. The graph may contain several components, including isolated vertices.

The outer loop examines every index `i`. When `color[i] == 0`, it starts a new DFS with color one. Each component may independently choose which physical side is called color one, so using the same initial sign for all components causes no restriction.

Already colored vertices are skipped because their entire connected component was explored when they first received a color.

An isolated vertex has no neighbor constraints. Its DFS colors it, scans an empty adjacency list, and returns true. It may be placed in either partition.

**Trace the bipartite example**

For `graph = [[1,3],[0,2],[1,3],[0,2]]`, start vertex zero with color one. Vertices one and three receive color negative one. From vertex one, vertex two receives color one.

Every remaining edge connects opposite signs. The sets are `{0, 2}` and `{1, 3}`, so the method finishes and returns true.

**Trace a triangle conflict**

Consider edges forming triangle zero-one-two-zero. Start zero with color one, color one as negative one, and color two as one through the path from vertex one.

The edge from vertex two back to vertex zero now has color one at both endpoints. The direct equality test returns false. This matches the impossibility of alternating two colors around a cycle of odd length.

**The recursive invariant**

When `dfs(a, c)` begins, `a` has been assigned the color required by the path through which it was discovered. While it scans neighbors, every processed incident edge has either been verified to connect opposite existing colors or has led to a recursively and consistently colored region.

If the call returns true, all edges reachable through its exploration are consistent with the developing two-coloring. If it returns false, it found a same-color edge somewhere in that component, which proves no bipartition exists there.

**Why the final result is correct**

If the algorithm returns false, an edge conflict proves that its component cannot be two-colored, so the entire graph is not bipartite.

If it reaches the final return, the outer loop has covered every component and DFS has verified every adjacency. Put all color-one vertices in one set and all color-negative-one vertices in the other. No edge has equal-colored endpoints, so both sets are independent and the graph is bipartite.

## Complexity detail

Let $V$ be the number of vertices and $E$ the number of undirected edges. Each vertex is colored once. Its adjacency list is scanned during that one DFS visit. Because every undirected edge appears in two adjacency lists, total time is $O(V + E)$.

The color array uses $O(V)$ space. In the worst case, recursive DFS can follow a path containing all vertices, so the call stack also uses $O(V)$ space. Total auxiliary space is $O(V)$.

## Alternatives and edge cases

- **Breadth-first coloring:** A queue can propagate the same opposite-color rule iteratively in $O(V + E)$ time and $O(V)$ space, avoiding recursion-depth concerns.

- **Union-find with doubled sets:** Represent each vertex and its opposite side, then union edge constraints. It works but is more elaborate than direct traversal.

- **Check only one component:** Incorrect because an unvisited component may contain an odd cycle.

- **Isolated vertices:** They impose no edge constraint and are always harmless.

- **Acyclic graph:** Every forest is bipartite because no cycle can create contradictory path parity.

- **Even cycle:** Alternating colors returns consistently to the starting color.

- **Odd cycle:** Alternating colors creates a same-color edge and forces false.

- **Already colored opposite neighbor:** It is valid and must not be recursed into again.

- **Color sign choice:** Starting a component at one rather than negative one only swaps the two partition labels.
