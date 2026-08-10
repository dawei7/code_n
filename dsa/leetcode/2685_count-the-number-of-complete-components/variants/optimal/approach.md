## General

**First identify each connected component**

Completeness is a property of an entire connected component. The solution builds an undirected adjacency list `g` by appending both directions for every edge `[a, b]`.

It then starts depth-first search from every still-unvisited vertex. One DFS reaches exactly the vertices in that start's component because it follows every adjacency and never crosses a nonexistent edge.

Array `vis` prevents revisiting vertices and ensures each component is processed once.

**Collect two numbers during DFS**

The helper returns a pair:

- `x`, the number of vertices in the explored component;
- `y`, the sum of the adjacency-list lengths of those vertices.

At one vertex `i`, the local values begin as `x = 1` and `y = len(g[i])`.

For each unvisited neighbor, recursion returns that neighbor subtree's pair, and the caller adds both totals. When the starting call finishes, its accumulated pair covers the full component.

**Why `y` counts every edge twice**

An undirected edge between $u$ and $v$ appears once in `g[u]` and once in `g[v]`.

Adding all vertex degrees therefore counts that edge at both endpoints. If a component has $e$ undirected edges:

$$
y=2e.
$$

The solution intentionally uses this doubled count, avoiding division and keeping the comparison integral.

**The degree sum of a complete component**

A complete graph with $a$ vertices contains one edge for every unordered pair:

$$
e=\binom{a}{2}=\frac{a(a-1)}{2}.
$$

Doubling gives:

$$
2e=a(a-1).
$$

Therefore the component is complete exactly when `b == a * (a - 1)`, where `a` and `b` are the DFS vertex and degree totals.

The exact code writes `ans += a * (a - 1) == b`. In Python, the Boolean comparison is 1 when true and 0 when false, so it increments only for complete components.

**Why equal edge count is sufficient**

The DFS has already established that these $a$ vertices form one connected component. The input is a simple graph: there are no self-loops and no repeated edges.

Among $a$ vertices, at most one edge can exist for each of the $a(a-1)/2$ pairs. Reaching this maximum edge count means every possible pair is present.

Thus equality cannot be caused by duplicated edges hiding a missing pair.

**Trace a complete triangle**

Vertices 0, 1, and 2 have edges `0-1`, `0-2`, and `1-2`.

DFS counts three vertices. Each has degree two, so the degree sum is six.

The required value is:

$$
3(3-1)=6.
$$

Equality holds, and this component contributes one to the answer.

**Trace a connected but incomplete component**

Consider vertices 3, 4, and 5 with only edges `3-4` and `3-5`.

Their degrees are two, one, and one, so `b = 4`. A complete three-vertex component requires six.

DFS still groups them correctly as one connected component, but the degree comparison rejects it because edge `4-5` is absent.

**Isolated vertices are complete**

An isolated vertex forms a connected component of size one. There are no pairs of distinct vertices that need an edge.

DFS returns `a = 1` and `b = 0`. The formula gives `1 * 0 = 0`, so the component is counted as complete.

This correctly handles vertices that never appear in `edges`. Accessing `g[i]` through the default dictionary yields an empty adjacency list.

**The DFS invariant**

When `dfs(i)` returns, every vertex reachable through unvisited adjacency edges from `i` has been marked, `x` equals their count, and `y` equals their total degree in the original graph.

The base contribution accounts for `i`. Recursive calls cover disjoint sets because vertices are marked before exploring neighbors. Adding their results covers the component exactly once.


The outer loop starts DFS once per connected component. For that component, DFS returns its exact vertex count $a$ and doubled edge count $b$.

By the complete-graph edge formula and the simple-graph guarantee, `b = a(a-1)` holds exactly for complete components. The Boolean addition counts precisely those components, so the final answer is correct.

**Why checking only connectivity is insufficient**

Every component found by DFS is connected by definition, but connected does not mean complete. A path of three vertices is connected while missing an edge between its endpoints.

The degree-sum condition supplies the additional all-pairs requirement without explicitly checking every vertex pair.

## Complexity detail

Building adjacency lists takes $O(e)$ time for $e$ edges. Across all DFS calls, each of $n$ vertices is visited once and each undirected edge is examined from both endpoints, so traversal takes $O(n+e)$. Total time is $O(n+e)$.

The adjacency lists use $O(n+e)$ space, the visited array uses $O(n)$, and recursive calls may reach depth $O(n)$. Total auxiliary space is $O(n+e)$.

## Alternatives and edge cases

- **Check every pair inside each component:** Correct but can require $O(a^2)$ work per component.
- **Verify every vertex degree equals component size minus one:** Also linear after collecting component vertices and is equivalent for a simple connected graph.
- **Breadth-first search:** Can gather the same vertex and degree totals iteratively, avoiding recursion depth.
- **Disjoint-set union:** Can group vertices and then compare component sizes with edge counts, but requires more bookkeeping.
- **Isolated vertex:** Counts as a complete one-vertex component.
- **Two vertices with one edge:** Their degree sum is two, matching `2 * 1`, so the component is complete.
- **Two isolated vertices:** They are two separate complete components, not one two-vertex component.
- **Missing one edge:** The degree sum is two below the complete requirement and the component is rejected.
- **No repeated edges:** Essential for maximum edge count to imply every pair exists.
- **No self-loops:** Ensures degrees correspond only to distinct-vertex pairs.
- **Recursive depth:** Small repository constraints are safe; iterative traversal is more robust for a much larger graph.
- **Boolean arithmetic:** Python converts true to one and false to zero in `ans += condition`.
