## General

**Connectivity decides whether any walk exists.** In an undirected graph, two distinct vertices admit a walk exactly when they lie in the same connected component. The source first builds those components with a disjoint-set union structure, also called Union-Find.

Each vertex begins as its own parent with size one. `find(x)` follows parent links to a component representative and applies path compression, rewriting visited parents directly to the root. `union(a,b)` finds both roots and, when different, attaches the smaller component under the larger one. Union by size and path compression make long sequences of operations almost constant time.

The first edge loop ignores weights and calls `union(u,v)`. After it finishes, every connected component has one representative.

**Why one AND value describes every query inside a component.** Adding another edge weight to a bitwise AND can only keep bits or clear them; it can never set a cleared bit. Therefore, among walks inside one component, the smallest possible cost is obtained by including every component edge's weight in the AND.

At first this may sound impossible because a query asks for a walk from one particular source to one particular target. The definition allows vertices and edges to repeat. In an undirected connected component, a walk can start at the query source, detour through every edge and backtrack as needed, then finish at the target. Repeating an edge does not change the result because `w & w == w`. Thus a walk containing every component edge is achievable.

Conversely, every query walk uses only edges from its component. The AND over all component edges has every bit that survives in every edge, so it is less than or equal to the AND over any subset used by a particular walk. It is therefore a lower bound on every walk cost and is also achievable. This proves it is the minimum.

**Accumulate component edge weights.** Array `g` begins as `[-1] * n`. In Python's bitwise representation, -1 behaves as an all-one identity:

`-1 & w == w`

for every nonnegative edge weight. The second edge loop finds the final root of one endpoint and applies `g[root] &= w`. Both endpoints have the same root after all unions, so every edge contributes to exactly its component's accumulator.

Only root entries in `g` are meaningful. Nonroot entries may remain -1, but queries always access `g[a]` after `a = uf.find(u)`.

**Answer each query from precomputed state.** Helper `f(u,v)` first returns zero when the endpoints are identical. The local query contract states `s_i != t_i`, so this branch is normally unreachable, but it documents the source's choice for a zero-edge walk.

For distinct endpoints, it obtains representatives `a` and `b`. If they differ, no walk exists and the answer is -1. If they are equal, `g[a]` is the AND of every edge in their component and hence the minimum possible walk cost.

The final list comprehension applies this constant-sized query logic to every pair.

**Trace the first example.** Vertices 0, 1, 2, and 3 form one component with edge weights 7, 7, and 1. Its accumulator is `7 & 7 & 1 = 1`. The query from 0 to 3 returns one. Vertex 4 has a different representative, so the query from 3 to 4 returns -1.

The walk in the reference detours from 1 to 2 and back before reaching 3. That detour is exactly why the low-weight edge may participate even though it is not on a simple path between the endpoints.

**Parallel edges and cycles.** Every edge row is included in the component AND, even when its endpoints were already united. This is essential: a non-tree edge can clear additional bits and can be traversed in an allowed walk. The first union loop may ignore its connectivity effect, but the second loop never ignores its weight.

## Complexity detail

Let $m$ be the number of edges and $q$ the number of queries. There are $O(m+q)$ Union-Find operations. With path compression and union by size, each has amortized $O(\alpha(n))$ time, where $\alpha$ is the inverse Ackermann function. Initialization costs $O(n)$.

The complete bound is $O((n+m+q)\alpha(n))$, commonly treated as almost linear. The second edge pass performs one find per edge, and every query performs at most two finds.

Parent, size, and component-AND arrays each use $O(n)$ space. The returned answer uses $O(q)$ output space. Excluding output, auxiliary space is $O(n)$.

## Alternatives and edge cases

- **DFS or BFS components:** Traverse adjacency lists and AND all edge weights in each component. This is $O(n+m+q)$ time but stores $O(n+m)$ graph structure.
- **Merge AND values during union:** It is possible with careful handling of edges inside already merged components, but a clean second pass avoids mistakes.
- **Disconnected endpoints:** Different roots produce -1 immediately.
- **Component with one low-weight edge:** That edge can clear many bits for every connected query through a detour.
- **Cycle edge:** It must contribute to the AND even though DSU connectivity does not need it.
- **Parallel edges:** Both weights contribute because a walk may traverse both.
- **Repeated traversal:** It does not change an AND because the operation is idempotent.
- **Isolated vertex:** Its accumulator stays -1, but distinct-vertex queries cannot connect to it; same-vertex behavior is handled before reading `g`.
- **Same endpoint:** The source returns zero, although the stated queries use distinct endpoints.
- **Zero-weight edge:** It makes the entire component's minimum query cost zero.
- **All equal weights:** The component accumulator remains that common weight.
- **Why -1 is an identity:** Python's infinite leading one bits make `-1 & w` equal `w` for nonnegative `w`.
- **Root changes during unions:** Costs are accumulated only after all unions, so every edge uses the final representative.
- **No adjacency list:** DSU avoids storing both directions of every edge.
- **Output reuse:** Every pair in one component shares the same precomputed answer.
