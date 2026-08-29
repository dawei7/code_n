## General

**A component is discovered by one complete graph traversal.**

Two vertices belong to the same connected component when some path of undirected edges connects them. Starting a depth-first search from one vertex follows every reachable edge, then every edge reachable from those neighbors, and so on. Therefore, after that search finishes, every vertex in the start vertex's component has been visited.

This leads to a counting rule: scan all vertices, and start a new search only when the current vertex has never been reached before. Each such new search discovers one previously unseen component. Vertices encountered later from that same component are already marked and do not increase the count.

The exact optimal source expresses this rule compactly by making `dfs(i)` return `1` when `i` begins a new traversal and `0` when `i` was already visited. Summing `dfs(i)` over every vertex then gives the number of components.

**Build the graph in both directions.**

The input supplies endpoint pairs rather than an adjacency structure. The source creates `g`, a list containing one neighbor list for every vertex from `0` through `n - 1`. For each edge `[a,b]`, it performs both updates:

- append `b` to `g[a]`;
- append `a` to `g[b]`.

Both are necessary because the graph is undirected. If only the first direction were stored, reachability would depend on the arbitrary endpoint order used in `edges`. For example, an input edge written as `[1,0]` must still allow a traversal starting at `0` to reach `1`.

An isolated vertex naturally has an empty neighbor list. It is still present in `g`, because `g` is created from `n`, not merely from vertices mentioned in `edges`. This ensures isolated vertices are counted as one-vertex components.

**Meaning and behavior of `dfs(i)`.**

The set `vis` contains every vertex that has already been claimed by a traversal. On entry, the helper first asks whether `i` is in that set.

If it is, `dfs(i)` immediately returns `0`. No new component began, and there is no reason to explore the same neighbors again. This early return is also what prevents infinite recursion in an undirected graph. Every stored edge can lead back to the vertex from which the search just came, and cycles can lead to many previously seen vertices.

If `i` is not visited, the helper adds it to `vis` before following any edge. Marking before recursion is crucial. If marking were delayed until after the neighbor loop, an edge from `i` to `j` could recurse from `j` straight back to the still-unmarked `i`, causing repeated recursion.

The helper then calls `dfs(j)` for every neighbor `j` in `g[i]`. It does not check `j in vis` in the loop itself; the called helper performs that check at its entrance. Return values from these neighbor calls are deliberately ignored. A neighbor reached during the current traversal belongs to the same component as `i`, so it must not be counted as a separate component even if that neighbor was previously unseen. Only the outer scan's fresh roots contribute to the answer.

After all reachable neighbors have been explored, the original fresh call returns `1`. That value means “this call started discovery of one component,” not “this component contains one vertex.” Regardless of whether the traversal reaches one vertex or hundreds, its root contributes exactly one.

**Walk through the first example.**

For `n = 5` and `edges = [[0,1],[1,2],[3,4]]`, the adjacency lists describe two groups: vertices `0,1,2` and vertices `3,4`.

The outer generator first calls `dfs(0)`. Vertex `0` is fresh, so it is marked. Its edge reaches `1`, which is marked and reaches `2`. Calls that follow edges back to already visited vertices immediately return `0`. Once this traversal finishes, `vis` contains `{0,1,2}`, and the root call returns `1`.

Next, `dfs(1)` and `dfs(2)` each return `0` immediately because the first traversal already reached them. Calling `dfs(3)` starts a second fresh traversal, marks both `3` and `4`, and returns `1`. Finally, `dfs(4)` returns `0`. The sum is therefore

$$
1 + 0 + 0 + 1 + 0 = 2.
$$

**Why one traversal reaches exactly one component.**

Every vertex visited by a search from root $r$ is connected to $r$: the recursion reaches that vertex by following a sequence of actual graph edges, and that sequence forms a path. Thus the search cannot cross into a different component.

Conversely, take any vertex $v$ in the same component as $r$. By the definition of connectivity, there is a path

$$
r = p_0, p_1, \ldots, p_t = v.
$$

The adjacency list stores every edge of that path in both directions. After visiting $p_0$, DFS examines $p_1$; after visiting $p_1$, it examines $p_2$; continuing along the path eventually visits $v$. Therefore the search cannot leave behind an unvisited vertex from its component.

Together, these directions prove that a fresh DFS marks exactly the vertices of one connected component.

**Why summing the return values counts all components once.**

The outer expression evaluates `dfs(i)` for every label from `0` through `n - 1`. Consider any component. Its smallest-scanned vertex, or more generally its first vertex reached by this outer order, is unvisited and produces `1`. That call marks the entire component. Every later outer call on a vertex in the component produces `0`. Hence each component contributes exactly one to the sum.

No component can be missed because every vertex appears in the outer range, including vertices absent from all edges. No component can be counted twice because the visited set persists across all calls.

## Complexity detail

Let $V=n$ be the number of vertices and let $E$ be the number of undirected edges. Creating the $V$ empty adjacency lists costs $O(V)$. Adding both endpoints for every input edge costs $O(E)$.

Across all traversals, each vertex becomes visited once. The neighbor loops inspect every stored adjacency entry once; because every undirected edge is stored twice, this is $2E$, still $O(E)$. Set membership and insertion are expected $O(1)$ operations. The exact implementation therefore takes $O(V+E)$ expected time.

The adjacency list occupies $O(V+E)$ space, the visited set stores up to $V$ labels, and recursive DFS can use up to $O(V)$ call frames on a long path. Total auxiliary space is $O(V+E)$.

The variant manifest currently describes a union-by-size disjoint-set method with $O(V + E\alpha(V))$ time and $O(V)$ space. That is not the checked-in optimal source: the source builds an adjacency list and runs recursive DFS. Its actual bounds are consequently $O(V+E)$ time and $O(V+E)$ space, and the explanation follows that exact code.

## Alternatives and edge cases

- **Iterative depth-first search:** Use an explicit stack instead of recursive calls. It has the same $O(V+E)$ time and space bounds and follows the same component-counting proof, while avoiding language recursion-depth limits.

- **Breadth-first search:** A queue can explore every vertex reachable from each fresh root. BFS also counts components in $O(V+E)$ time and uses $O(V+E)$ total storage including the graph. Traversal order changes, but the discovered component does not.

- **Disjoint set union:** Begin with $V$ components and union the endpoints of each edge, decrementing the count only when two different sets merge. With path compression and union by size, this uses $O(V)$ extra space without an adjacency list and takes $O(V + E\alpha(V))$ time. It matches the current manifest summary but is not the exact optimal solution file.

- **Isolated vertices:** A vertex with no incident edge is never reached from another vertex. Its outer `dfs` call is fresh, returns `1`, and correctly counts a singleton component.

- **One connected chain:** When edges connect every vertex in a single path, the first DFS marks all vertices and every later outer call returns `0`, giving one component.

- **Cycles:** A cycle does not create an extra component or infinite traversal. Vertices are marked before their neighbors are explored, so any edge back into the visited region stops immediately.

- **No repeated edges and no self-loops:** The contract excludes both, but the algorithm would still count correctly if either appeared. They would only add redundant adjacency entries that lead to already visited vertices.

- **Recursive depth in Python:** The constraint permits up to `2000` vertices. A path-like component can create one recursive frame per vertex, which may exceed Python's default recursion limit. Replacing the helper with an explicit stack would preserve the algorithm while removing this implementation-level risk.

- **Outer calls on visited vertices:** Calling `dfs` unconditionally inside `sum` is intentional. The immediate `0` return makes these calls constant-time checks and turns the helper's result directly into the component indicator.
