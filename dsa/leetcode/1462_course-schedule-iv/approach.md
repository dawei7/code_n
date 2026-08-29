## General

**Model prerequisites as directed reachability.** A direct pair `[a, b]` creates an edge from course `a` to course `b`. Course `a` is also an indirect prerequisite of `b` whenever some directed path leads from `a` to `b`. Each query is therefore a reachability question.

Because many queries use the same graph, the solution precomputes reachability for every ordered pair. The Boolean matrix `f` has `n` rows and columns. `f[a][b]` is true when the algorithm knows a path from `a` to `b`.

The direct prerequisite loop establishes the initial paths of length one by assigning `f[a][b] = True`. All other entries begin false. The graph has no cycles and queries use different courses, so the diagonal does not need to represent a course as its own prerequisite.

**Introduce possible intermediate courses one at a time.** The three nested loops are the Boolean form of Floyd–Warshall. The outer variable `k` is the next course allowed as an intermediate point. For every source `i` and destination `j`, if `i` can reach `k` and `k` can reach `j`, then concatenating those two paths proves `i` can reach `j`.

The condition `if f[i][k] and f[k][j]` performs exactly that test. When it succeeds, `f[i][j] = True` records the newly proven indirect prerequisite relation. A true entry is never changed back to false.

**Why k must be the outer loop.** After finishing outer iteration `k`, the matrix represents paths whose internal vertices come only from courses zero through `k`. When evaluating paths through `k`, both smaller pieces have already been established using earlier allowed intermediates.

If the loops were reordered arbitrarily, a relation needed later in the same closure process might not yet be available, and one pass would not necessarily discover all path lengths. The outer-intermediate order gives the standard inductive guarantee.

**Trace a short chain.** With direct pairs `[1, 2]` and `[2, 0]`, initialization marks `f[1][2]` and `f[2][0]`. When course two is considered as an intermediate, both halves of path `1 -> 2 -> 0` are true, so `f[1][0]` becomes true. Queries for `1, 0` and `1, 2` then return true, while the reverse directions remain false.

Longer chains are discovered in the same manner. A path can be split around its highest-numbered internal course under the current ordering; the two halves were available by the time that intermediate is processed.

**Answer queries with direct lookups.** After closure, every `f[a][b]` already contains the answer. The list comprehension preserves query order and returns one Boolean per input pair. No graph traversal is repeated per query.

**Why closure is correct.** Initially, every true entry corresponds to a real direct edge. Every later assignment combines two real paths, so it also corresponds to a real path; the algorithm never creates a false prerequisite relation.

For completeness, consider any path from `i` to `j`. If it has no internal vertex, initialization records it. Otherwise, take its internal vertex with the largest index under the Floyd ordering. When that course is the outer intermediate, the path segments before and after it use only earlier allowed internal vertices and have already been recorded. Their conjunction sets `f[i][j]`. Hence every direct or indirect prerequisite is eventually true.

**Be precise about the advertised complexity.** The manifest states `O(CE + C + Q)`, which corresponds to running a graph search from each of `C` courses over `E` edges. The exact stored source always executes three loops of size `C`, regardless of graph sparsity. Its actual running time is `O(C^3 + E + Q)`.

Its `O(C^2)` reachability storage agrees with the dominant matrix part of the manifest. No adjacency list is created in this exact implementation.

## Complexity detail

Let `C` be the number of courses, `E` the number of direct prerequisites, and `Q` the number of queries. Matrix allocation takes `O(C^2)` time and space. Loading edges takes `O(E)`.

The three closure loops execute `C^3` iterations with constant-time Boolean checks and occasional assignments. Answering queries takes `O(Q)`. Total exact time is `O(C^3 + E + Q)`, normally simplified to `O(C^3 + Q)` because `E <= C^2`.

The matrix uses `O(C^2)` space, and the returned answer uses `O(Q)` output space. Excluding output, auxiliary space is `O(C^2)`.

For sparse graphs, DFS or BFS from every course takes `O(C(C + E) + Q)` time, equivalent in spirit to the manifest's `O(CE + C + Q)` notation, but that is not the control flow stored here.

## Alternatives and edge cases

- **Search from every course:** Build an adjacency list and run DFS or BFS from each source, recording reachable courses. This can exploit sparsity and matches the manifest more closely.
- **Search per query:** It avoids a full closure when there are very few queries, but repeats graph work when queries share sources.
- **Topological propagation:** Because the graph is acyclic, process courses in topological order and union prerequisite sets into successors. It can be efficient with bitsets.
- **Bitset Floyd closure:** Store each reachability row as an integer or bitset and union rows when an intermediate is reachable, improving constants substantially.
- **No prerequisites:** The matrix stays false and every valid query returns false.
- **Direct prerequisite:** Initialization makes it true even without an intermediate.
- **Long indirect chain:** Closure composes successive path pieces until the first course reaches the last.
- **Multiple paths:** Reachability is Boolean, so discovering the same relation more than once has no effect.
- **Disconnected components:** No conjunction bridges them, so cross-component queries remain false.
- **Acyclic guarantee:** There is no mutual prerequisite cycle. The algorithm would still compute reachability on a cyclic graph, but diagonal semantics would need definition.
- **Queries use distinct courses:** The source can read `f[a][b]` directly without deciding whether a course counts as its own prerequisite.
- **Duplicate prerequisite outside the contract:** Assigning the same Boolean again would be harmless.
- **Query order:** The list comprehension preserves the original sequence exactly.
- **Dense graph:** Floyd–Warshall's fixed cubic work is reasonable for the small course limit and many queries.
- **Complexity reporting:** Use `O(C^3 + E + Q)` for this exact source, not the sparse-search manifest bound.
