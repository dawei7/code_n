## General

**Use the functional-graph structure**

Each node has at most one outgoing edge. Therefore, once a traversal starts at a node, its future is deterministic: it repeatedly follows one next node until it reaches `-1` or encounters a node seen before. There are no branches to explore.

A repeated node does not automatically mean that the current traversal found a new cycle. The repeated node might have been visited by an earlier outer-loop traversal. The algorithm must distinguish these situations:

- If the repeated node occurs in the path currently being recorded, the suffix beginning at its first occurrence is a cycle.
- If it was visited before but is absent from the current path, this path has merely joined an already processed component. Any cycle beyond that point was measured earlier.

The exact solution makes that distinction with a global Boolean array `vis` and a per-traversal list `cycle`.

**Start only from globally unvisited nodes**

The outer loop considers every node `i`. If `vis[i]` is already true, it skips that start. This is safe because the graph has only one outgoing edge per node. During the first visit, the algorithm already followed that node's only possible future until termination or repetition. Starting from it again cannot reveal an alternate branch or a different cycle.

For a new start, `j = i` and `cycle = []`. Despite the variable's name, this list initially stores the entire current walk, including any non-cyclic prefix. During the loop, the algorithm:

1. marks `j` globally visited;
2. appends `j` to the current traversal list;
3. advances with `j = edges[j]`.

The loop continues only while `j != -1` and `vis[j]` is false. Every newly appended node is therefore unique within this walk and had never been processed by an earlier walk.

**Interpret how the walk stopped**

If `j == -1`, the path reached a node with no outgoing edge. Such a path contains no cycle, so the solution continues to the next outer-loop start.

Otherwise, `j` is globally visited. Let `m = len(cycle)`. The expression

```python
next((k for k in range(m) if cycle[k] == j), inf)
```

searches for `j` inside the current list and returns its first index `k`. If `j` belongs to the current walk, the nodes

```text
cycle[k], cycle[k + 1], ..., cycle[m - 1]
```

form the cycle. The last node points back to `cycle[k]`, so its length is `m - k`.

For example, suppose the walk list is `[0, 1, 2, 4, 3]` and the next node is `2`. The repeated node first appears at index `2`. The suffix `[2, 4, 3]` is the cycle, and `m - k = 5 - 2 = 3`.

If `j` was visited by an earlier traversal, it is not in the current list. The generator finds no index, so `next(..., inf)` returns `inf`. Then `m - k` is negative infinity. Taking `max(ans, m - k)` leaves the finite current answer unchanged. This is an unusual but compact way for the exact solution to ignore a path that merges into old work without writing a separate membership test.

**Why global visitation cannot hide a longer cycle**

Suppose a new path reaches a node marked by an earlier traversal. From that node onward, both traversals must follow the same edges because each node has at most one outgoing edge. The earlier traversal therefore already examined the complete suffix. If that suffix contains a cycle, its length was calculated then; if it terminates at `-1`, the new path also cannot create a cycle after merging.

A non-cyclic prefix leading into a cycle is excluded by the index calculation. Only the suffix from the repeated node through the end of the current list is counted. This is exactly what cycle length means: prefix nodes are visited once and never returned to.

**Why every cycle is measured**

Take any cycle in the graph and consider the first outer-loop traversal that reaches one of its nodes. None of the cycle nodes could have been globally processed earlier; if one had, following its deterministic edges would already have processed the whole cycle. The current traversal proceeds around the cycle, marking and appending each node. After the last distinct cycle node, the next edge returns to the first cycle node encountered. That repeated node is present in `cycle`, so the algorithm computes the exact cycle suffix length.

Each cycle is therefore measured at least once. Global marking ensures it is not needlessly traversed again. `ans` starts at `-1` and is replaced by the maximum measured length. If no traversal ever repeats a node from its own current list, no cycle exists and the initial `-1` remains.

**A note about the constraints**

The contract says `edges[i] != i`, so one-node self-cycles do not occur. The algorithm would still handle one correctly: the list would contain that node, the next node would repeat index zero, and the computed length would be one. No special-case logic is needed.

## Complexity detail

Let $n$ be the number of nodes. Every node changes from unvisited to visited exactly once. The walking loops collectively append at most $n$ nodes, and the outer loop itself performs $n$ constant-time checks.

Whenever a traversal stops at a visited node, the generator may scan its current list to find that node. Current traversal lists are disjoint in their newly visited nodes, so the sum of their lengths is at most $n$. Each list is searched at most once, at the end of its traversal. Consequently, all these searches also take $O(n)$ total time rather than $O(n^2)$. The full time complexity is $O(n)$.

The global `vis` array occupies $O(n)$ space. A single `cycle` list can contain up to $n$ nodes, and old lists become unreachable after each outer iteration. Peak auxiliary space is therefore $O(n)$. The algorithm is iterative, so it does not add a potentially deep recursive call stack.

## Alternatives and edge cases

- **Three-state visitation:** Mark nodes as unseen, active in the current traversal, or completely processed. This detects current-path revisits in $O(1)$ without searching the list, but requires storing an entry time or depth to calculate length.
- **Traversal identifier and timestamps:** Arrays can record which traversal first saw each node and at what step. A repeated matching identifier proves that the node belongs to the current walk. This is often clearer than the `inf` sentinel trick.
- **Kahn's algorithm:** Repeatedly remove indegree-zero nodes. The remaining nodes belong to cycles, which can then be counted. It is also $O(n)$ but needs indegrees and a queue.
- **Recursive DFS:** Recursion can model active and finished states naturally, but a chain of length $10^5$ risks exceeding Python's recursion limit.
- **Path reaches `-1`:** No cycle closes, so the current list contributes nothing.
- **Path merges into earlier work:** The repeated node is absent from the current list, `k` becomes `inf`, and the maximum answer is unchanged.
- **Tail entering a cycle:** The index `k` excludes every tail node and counts only the repeated suffix.
- **Several disconnected cycles:** Separate unvisited starts discover them, and `max` retains the longest length.
- **Equal-length cycles:** Only the length is returned, so no tie-breaking by node is necessary.
- **No cycles anywhere:** `ans` is never raised above its initial value and the method returns `-1`.
