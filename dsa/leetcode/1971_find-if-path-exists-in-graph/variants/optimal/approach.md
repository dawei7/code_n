## General

**Represent the undirected graph with both directions**

The code creates one adjacency list per vertex. For every edge `[u, v]`, it appends `v` to `g[u]` and `u` to `g[v]`. A path can therefore traverse an edge in either direction.

The intended search is depth-first: starting from `source`, recursively search neighbors until `destination` is reached. `any(...)` short-circuits when a recursive call returns true.

**The required visited invariant**

In an undirected graph, every traversed edge immediately offers a route back to the parent. A correct DFS must mark a vertex visited before recursively exploring its neighbors. Revisiting a marked vertex should return false for that branch.

With that invariant, each reachable vertex is processed once. Reaching `destination` proves a path; exhausting all source-component vertices proves none exists.

**The exact source omits the marking operation**

The function creates `vis = set()` and checks:

`if i in vis: return False`.

However, it never executes `vis.add(i)`. The set remains empty forever. The visited check therefore cannot stop a back edge.

For a simple edge `0 -- 1` with source zero and an unreachable destination elsewhere, `dfs(0)` calls `dfs(1)`, which calls `dfs(0)` again, and recursion repeats until Python raises `RecursionError`. A longer cycle has the same problem.

Even an acyclic undirected graph has two-way adjacency, so parent-child backtracking is already a length-two recursion cycle unless the destination is found before that edge is followed.

The exact implementation may return true in favorable cases—for example, when source equals destination or a neighbor path reaches destination before any failing backtrack—and it returns false for an isolated nondestination source. But it is not a correct general solution.

**The minimal correction**

After the destination test and prior to exploring neighbors, insert:

`vis.add(i)`.

Then the check `if i in vis` prevents repeated processing. Alternatively, mark on entry before the destination test; either order is fine because reaching the destination should return true.

With this correction, `any(dfs(j) for j in g[i])` explores neighbors lazily. Failed visited or disconnected branches return false, and the first successful destination branch propagates true to the top.

**Why marking must happen before recursion**

It is not enough to add a vertex after all its neighbors have been explored. While the first call is still exploring, a neighbor can follow the reverse edge and enter the same vertex again. Marking immediately on entry records that exploration is already in progress and closes that back edge before it can recurse. This timing rule applies to recursive graph searches generally: claim a state before expanding transitions from it.


Every recursive call follows a real graph edge from a reachable vertex, so every visited vertex has a path from `source`. If the destination is reached, a valid path exists.

If corrected DFS finishes false, it has explored every vertex reachable from source exactly once. Destination was not among them, so no path exists.

This proof cannot be applied to the source as written because the visited-set invariant is never established. A beginner should not be asked to infer a missing line silently; the defect materially changes termination and correctness.

## Complexity detail

Building adjacency lists takes $O(V+E)$ time and space.

For the intended corrected DFS, each vertex is visited once and each undirected edge is examined from both endpoints, giving $O(V+E)$ time. The visited set, adjacency lists, and recursion stack use $O(V+E)$ total space.

For the exact source, no finite $O(V+E)$ execution bound applies on general inputs because recursion can repeat until a runtime error. Its call stack grows until Python's recursion limit rather than being bounded by a correct visited traversal. Even the corrected recursive version can exceed Python's recursion limit on a long path of up to $2\cdot10^5$ vertices; iterative DFS or BFS is safer.

## Alternatives and edge cases

- **Iterative DFS:** Use an explicit stack and mark vertices when pushed or popped. It avoids both the missing-mark bug and Python recursion limits.
- **Breadth-first search:** A deque explores the same connected component in $O(V+E)$ time and can stop when destination is reached.
- **Disjoint Set Union:** Union every edge, then compare representatives of source and destination. This is useful for repeated connectivity queries.
- **Source equals destination:** The exact code returns true before needing visited state, which is correct.
- **Isolated source:** If it is not the destination, `any` over an empty neighbor list returns false.
- **Single undirected edge away from destination:** The missing visited insertion causes immediate parent-child recursion.
- **Cycle:** The exact source can loop recursively around it until `RecursionError`.
- **Favorable neighbor ordering:** Reaching destination early may hide the bug on some true cases, but correctness must hold for all inputs.
- **No duplicate edges:** Adjacency still contains one entry in each direction, so visited marking remains essential.
- **Minimal fix:** Add `vis.add(i)` before the recursive neighbor search.
- **Recursion depth after fixing:** A chain can still exceed Python's call-stack limit; an explicit stack is production-safe.
