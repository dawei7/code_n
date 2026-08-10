## General

**The graph is a collection of paths feeding cycles.** Every node has exactly one outgoing edge, so starting anywhere produces one deterministic sequence. Eventually a node repeats because the graph is finite. The repeated portion is a directed cycle, while any earlier nodes form a tail leading into that cycle. The number of distinct visited nodes is

$$
\text{tail length}+\text{cycle length}.
$$

Different starting paths can also merge before reaching a cycle. Once a path reaches a node whose answer is already known, its remaining number of visits is known too.

The exact solution exploits both possibilities with arrays `vis` and `ans`. Despite the manifest's description of indegree pruning, this source does not compute indegrees or remove nodes. It discovers one successor path at a time and then writes answers backward.

**What the two arrays mean.** `ans[v] == 0` means node `v` has no completed answer yet. Every real answer is positive, so zero is a safe unresolved marker.

During a new unresolved traversal, `vis[v]` records the one-based position where `v` first appeared on that path. If the start is position one, its successor is position two, and so on. The array is not cleared between outer-loop iterations. That is safe because every node visited in a completed earlier traversal also receives a nonzero answer during that traversal. Therefore, encountering `vis[j] != 0` with `ans[j] == 0` can only mean that `j` belongs to the current path and a new cycle has just been closed.

**Walk until something repeats.** For an unresolved start `i`, the source initializes `cnt = 0` and `j = i`. While `vis[j]` is zero, it increments `cnt`, stores that step number in `vis[j]`, and follows `j = edges[j]`. The loop stops in one of two states.

If `ans[j]` is already nonzero, current path has merged into a previously solved path. There is no new cycle to measure. The total number of distinct nodes from `i` is the number `cnt` of newly walked nodes plus `ans[j]`, so `total = cnt + ans[j]` and `cycle` stays zero.

If `ans[j] == 0`, node `j` was first visited on this same walk at position `vis[j]`. The cycle contains positions `vis[j]` through `cnt`, inclusive, so its length is

`cycle = cnt - vis[j] + 1`.

The whole newly discovered path has `cnt` nodes, so `total = cnt` for the start.

**Write answers by following the path again.** The source resets `j = i` and follows successors while `ans[j]` is still zero. At each node it assigns

`ans[j] = max(total, cycle)`

and then decrements `total`.

Before the cycle, moving one step forward removes the current tail node from the distinct-visit count, so the answer decreases by one. Once `total` reaches the cycle length, every cycle node must still receive the full cycle length: starting at any cycle position visits every cycle node before repeating. The `max` prevents the decreasing tail count from dropping below `cycle`.

If the path merged into an already solved node, `cycle = 0`. The backward-writing pass assigns `cnt + ans[j]` to the start, one less to each successor, and stops upon reaching the existing nonzero answer. This is exactly the distance-to-known-node plus known suffix answer.

**Trace `edges = [1,2,0,0]`.** Starting at zero visits positions zero, one, and two, then returns to zero. The repeated zero was stamped at position one, so `cycle = 3 - 1 + 1 = 3`. All three cycle nodes receive answer three. When outer iteration reaches node three, it walks one new node and reaches already solved node zero. Its total is `1 + ans[0] = 4`, so `ans[3] = 4`.

**Why each node is processed only a constant number of times.** The discovery walk enters only nodes with `vis == 0`. The assignment walk fills every newly reached node's answer. Later outer-loop visits skip any start whose answer is nonzero. A node may be touched during discovery and assignment, but it never belongs to another unresolved traversal.

This path-stamping proof gives the same linear result as the more common “prune non-cycle nodes, label cycles, then propagate backward” method, but it is important to describe the source that actually executes.

## Complexity detail

Across all starts, each node is first stamped at most once and assigned an answer at most once. Following outgoing edges therefore totals $O(n)$ time, not $O(n)$ per start. Arrays `ans` and `vis` each contain $n$ integers, so auxiliary space is $O(n)$. The algorithm is iterative and has no recursion-depth risk.

The manifest's $O(n)$ time and space bounds are accurate, although its stated indegree-pruning algorithm is not. The input `edges` is only read and is not modified.

## Alternatives and edge cases

- **Indegree pruning:** Remove all indegree-zero nodes with a queue, leaving only cycles; assign cycle lengths, then process removed nodes in reverse. This matches the manifest summary and also runs in $O(n)$ time and space.
- **Three-color DFS:** Track unseen, active, and finished states to detect cycles, but recursive Python implementations risk stack overflow on a chain of length $10^5$.
- **Naive simulation per start:** A fresh visited set from every node can take $O(n^2)$ time because shared tails and cycles are rediscovered.
- **Path merging into solved work:** `cnt + ans[j]` reuses the complete known suffix without entering it again.
- **Pure directed cycle:** Every node receives the cycle length.
- **Long tail into a short cycle:** Answers decrease by one along the tail and become constant on the cycle.
- **Persistent `vis` values:** They need not be cleared because any node from an older traversal also has a completed `ans` value.
- **Self-loop:** The constraints exclude `edges[i] == i`, but the formula would still identify a cycle of length one correctly.
