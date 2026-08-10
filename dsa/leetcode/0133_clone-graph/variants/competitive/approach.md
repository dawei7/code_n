## General

**Clone nodes once and rebuild every adjacency reference**

The algorithm needs to reproduce a connected undirected graph using new objects. Copying only values is insufficient: the neighbor lists encode the graph’s edges, cycles, and shared destinations.

The dictionary `cloned` associates each original object with exactly one clone. Its first entry maps the supplied node to `cloned_node`. The list named `queue` stores original nodes whose outgoing neighbor lists still need to be processed.

Despite that variable name, `queue.pop()` removes from the end, so this is a LIFO stack and the traversal is iterative depth-first search, not breadth-first search. Traversal order has no effect on the final clone as long as every discovered node is eventually processed.

**Discover a node before scheduling it**

The starting clone is created and inserted before the loop. Each iteration removes one original `current` and scans `current.neighbors`.

When a neighbor has no dictionary entry, the code:

1. appends that original neighbor to the stack;
2. creates a new clone with the same label;
3. stores the original-to-clone association.

The clone is registered during discovery, before the neighbor is later processed. That timing prevents duplicate work. If several already processed nodes point to the same undiscovered neighbor, only the first encounter creates and schedules it; subsequent encounters find it in `cloned`.

After ensuring the neighbor clone exists, the algorithm appends it to `cloned[current].neighbors`. This append occurs for every original adjacency entry, whether the neighbor was new or already known. That is essential: the dictionary check governs node creation, not whether the edge should be copied.

In an undirected edge between `A` and `B`, processing `A` appends clone `B` to clone `A`. Later, processing `B` appends clone `A` to clone `B`. The dictionary makes the second reference point back to the already existing clone instead of producing a duplicate node.

**Why the copied structure matches the reachable graph**

There is one clone per original because construction occurs only when the original is absent from `cloned`, followed immediately by insertion. Every future encounter reuses the stored object.

Every original adjacency entry is reproduced. Every discovered original is pushed exactly once and later popped, and its entire neighbor list is scanned. For each list entry, the corresponding clone reference is appended to the current clone’s list in the same order.

Every clone adjacency points to another clone, never to an original. The append uses `cloned[neighbor]`, while original objects appear only as dictionary keys and stack elements. This proves the copy is independent.

Because the input graph is connected, repeatedly following adjacency entries from the supplied node reaches all vertices. The algorithm therefore creates the complete graph. It returns `cloned[node]`, the new entry node rather than the original.

For a cycle, discovery marking stops repeated scheduling. For an isolated node, the stack processes one empty neighbor list and returns the single clone. For `None`, the early branch returns `None`.

**The legacy interface in this selected source**

This file defines `UndirectedGraphNode` with fields `label` and `neighbors`, and `cloneGraph` reads `node.label`. That matches an older version of the platform contract.

The current Reference describes a platform-provided `Node` with fields `val` and `neighbors`. Therefore, this source is algorithmically correct for its declared legacy node type but is not directly compatible with the current native `Node` interface: a current node has `val`, not necessarily `label`, and the returned object is the legacy class rather than `Node`.

To adapt the same algorithm to the current contract, node construction must use the platform-provided `Node`, and values must be read through `node.val`. That is an interface correction, not an algorithmic change.

## Complexity detail

Let $V$ be the number of vertices reachable from the input and $E$ the number of undirected edges.

Every original vertex is pushed and popped once because it is entered into `cloned` upon first discovery. Its neighbor list is scanned once. Undirected adjacency represents each edge twice, so the total scanned entries are $2E$, yielding $O(V+E)$ time with expected constant-time dictionary operations.

The dictionary and explicit stack each hold at most $V$ references, so auxiliary working space excluding the clone is $O(V)$. The returned graph contains $V$ new nodes and $O(E)$ neighbor references. When output storage is counted, total space is $O(V+E)$, which matches the manifest. The file’s short `O(n)` comment is consistent if `n` means the complete input representation size rather than vertices alone.

The stack uses iterative traversal, so there is no recursive call-stack risk. LIFO versus FIFO affects only processing order, not the asymptotic bounds.

## Alternatives and edge cases

- **Breadth-first traversal:** Replace the list with `collections.deque` and remove with `popleft`. It produces the same clone mapping while visiting vertices by graph distance.
- **Recursive depth-first traversal:** Return a neighbor’s clone recursively after registering the current clone. It is concise but may exceed the recursion limit on a long graph.
- **Two explicit passes:** First create clones for all reachable nodes, then copy every neighbor list. This separates identity creation from edge construction at the cost of a second traversal.
- **Map by unique label:** The constraints make labels unique, but object-keyed mapping is safer because topology is fundamentally about node identity.
- **Empty graph:** `None` returns `None` before any field access.
- **Isolated node:** The starting clone is processed once and retains an empty neighbor list.
- **Undirected cycles:** Mark-on-discovery prevents endless repetition even though each edge appears in both directions.
- **Neighbor order:** The loop appends in source-list order. Although adjacency-list equality often ignores order, preserving it is a useful fidelity property.
- **No self-loops or repeated edges:** The contract excludes both. If present, the algorithm would preserve them rather than silently normalize the graph.
- **Legacy/current mismatch:** `label` and `UndirectedGraphNode` must be replaced by `val` and the platform `Node` for the current Reference contract.
- **Misleading container name:** Calling the list `queue` does not make the traversal BFS; `pop()` is LIFO. Using `pop(0)` would be FIFO but inefficient for Python lists.
- **Hashability:** The implementation assumes original node objects can be dictionary keys, as standard identity-based node objects can.
