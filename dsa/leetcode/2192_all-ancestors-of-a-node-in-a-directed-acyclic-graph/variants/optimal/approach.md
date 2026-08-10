## General

A node `s` is an ancestor of every node reachable by following directed edges outward from `s`. The exact solution uses that definition directly:

1. build the original forward graph;
2. start one breadth-first traversal from every possible source `s`;
3. whenever that traversal first reaches node `j`, append `s` to `ans[j]`.

Running sources in numeric order automatically produces each ancestor list in ascending order.

**Build forward adjacency**

For every edge `[u, v]`, the code appends `v` to `g[u]`. Traversing neighbors from `u` therefore follows the original edge direction toward descendants.

A `defaultdict(list)` supplies an empty neighbor list for a node with no outgoing edges, so BFS needs no special membership test.

**Give each source an independent traversal**

Helper `bfs(s)` begins with queue `deque([s])` and visited set `{s}`.

The queue contains reached nodes whose outgoing edges still need examination. Marking a node visited when it is enqueued ensures it enters the queue at most once during this source's traversal.

The visited set is new for every `s`. Reachability from one source must not suppress traversal from another because the goal is to record all ancestors separately.

**Append the source only on first reach**

When edge `i -> j` leads to an unvisited node `j`, the code:

- adds `j` to `vis`;
- enqueues `j` so its descendants are explored;
- appends source `s` to `ans[j]`.

The first discovery proves there is a path from `s` to `j`: the queue reached `i` through a path from `s`, and the edge extends it.

If another path from the same source later reaches `j`, the visited test skips it. An ancestor should appear once in a node's result even when several directed paths connect them.

**Why a node is not listed as its own ancestor**

Source `s` is placed in `vis` initially but is not appended to `ans[s]`. In a DAG, no directed path can leave `s` and return to it, so it will never be rediscovered.

This matches the intended ancestor relation for the acyclic graph: results contain proper upstream nodes, not the node itself.

**Why BFS discovers every descendant**

The queue starts at `s`. Whenever a reached node is processed, every outgoing edge is examined and every unseen endpoint is added.

By induction on path length, all nodes one edge away are reached, then all nodes two edges away, and so on. Every descendant has some finite directed path and is eventually discovered.

Conversely, the only way into the queue is through an outgoing edge from an already reachable node, so every discovered node is truly reachable from `s`.

Thus `s` is appended to exactly the result lists for which it is an ancestor.

**Get sorted lists without sorting**

The outer loop calls `bfs(i)` for `i = 0, 1, ..., n - 1`. Whenever a result list receives values, those source values arrive in this ascending outer-loop order.

Traversal order inside a BFS does not affect that property: one source either appends itself once to a given node or not at all before the next source begins.

Therefore every `ans[j]` is already sorted ascending, and no final sorting pass is necessary.

**Why the entire answer is exact**

Take any value `s` appended to `ans[j]`. It was appended on BFS discovery, which establishes a path from `s` to `j`, so it is a valid ancestor.

Conversely, if `s` is an ancestor of `j`, forward BFS from `s` reaches `j` along some path and appends `s` on its first discovery. The visited set prevents duplicates, and ascending source iteration supplies the required ordering.

Nodes with no ancestors never receive an append, so their pre-created empty lists remain correct.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of directed edges. One BFS can visit $O(n)$ nodes and scan $O(m)$ edges in the worst case, taking $O(n+m)$ time.

Running it from all $n$ sources costs

$$
O(n(n+m))=O(n^2+nm).
$$

The adjacency lists use $O(n+m)$ space. One queue and visited set use $O(n)$. The answer can contain $O(n^2)$ ancestor entries, so total storage including output is $O(n^2+m)$, matching the manifest.

The same queue and visited objects are replaced between sources rather than retained simultaneously, so traversal working space does not multiply by $n$.

## Alternatives and edge cases

- **Topological propagation:** Process nodes in topological order and union each node's ancestors into its children. This can exploit the DAG structure but needs potentially large sets.
- **Reverse-graph traversal per target:** Starting from each target in a reversed graph directly collects its ancestors, followed by sorting or numeric scanning.
- **Bitset propagation:** With $n\le1000$, machine-word bitsets can make ancestor unions efficient, then set bits can be emitted in order.
- **Isolated node:** Its BFS reaches only itself and appends nothing, so its ancestor list is empty.
- **Multiple paths from one source:** `vis` ensures the source appears only once in the descendant's list.
- **Several sources:** Independent traversals append each valid ancestor separately.
- **No edges:** Every BFS immediately ends and all result lists stay empty.
- **Dense DAG:** Output itself can contain $\Theta(n^2)$ entries, making quadratic storage unavoidable.
- **Ascending requirement:** Numeric source-loop order provides sorted output without sorting adjacency lists.
- **Adjacency order:** It affects discovery sequence within one BFS but not result ordering across sources.
- **Acyclic guarantee:** No node is its own ancestor through a cycle; visited would still prevent infinite traversal.
- **Defaultdict side effect:** Reading a sink's adjacency creates an empty list entry but does not affect graph meaning.
- **Input preservation:** The edge list is only read to build separate adjacency lists.
