## General

**Combine topological sorting with path dynamic programming.** In a directed acyclic graph, every path into a node comes from a predecessor that can be processed earlier in topological order. The solution maintains, for every node `i` and color `k`, the best number of occurrences of that color on any path ending at `i`.

`dp[i][k]` has 26 entries because colors are lowercase English letters. Keeping all colors is necessary: the color that becomes most frequent on the globally best path may differ from the current node’s color.

**Build graph and indegrees.** For every directed edge `a -> b`, `g[a].append(b)` records the outgoing neighbor and `indeg[b] += 1` counts one unmet predecessor. Nodes whose indegree is zero can begin topological processing immediately.

For each such source node, the code sets its own color count to one in `dp` and enqueues it. A one-node path is valid, so this is the correct base case.

**Process nodes with Kahn’s algorithm.** The deque contains nodes whose predecessors have all been removed from the graph logically. Popping node `i` increments `cnt`, the number of topologically processed nodes.

For each edge `i -> j`, the code decreases `indeg[j]`. When it reaches zero, every predecessor of `j` has already propagated its path information, so `j` is enqueued.

**Propagate all 26 color counts across an edge.** Let `c` be the numeric color index of destination `j`. A path ending at `i` can be extended to `j`. For each color `k`, its count becomes:

`dp[i][k] + 1` if `j` has color `k`, otherwise `dp[i][k]`.

The assignment takes the maximum with the value already accumulated in `dp[j][k]` because `j` may have several predecessors, each offering a different best path.

The update occurs for every incoming edge, even if `j` has not yet reached indegree zero. By the time it is queued, all incoming candidates have been merged.

**Track the best answer during propagation.** `ans` begins at one because the graph has at least one node and every single-node path has color value one. Each updated `dp[j][k]` may improve it. Isolated source nodes need no explicit answer update because one is already recorded.

**Trace the path with repeated color.** In `colors = "abaca"`, source node zero starts with one occurrence of `a`. Propagating through node two adds another `a`, node three preserves that count because its color differs, and node four adds the third `a`. `dp[4]["a"]` becomes three, so `ans` becomes three.

**Cycle detection comes from the processed count.** A directed cycle has no point at which all nodes in that cycle reach indegree zero. Kahn’s algorithm therefore processes fewer than `n` nodes. The return expression yields minus one when `cnt < n`, even if some acyclic portion produced a large temporary color value.

Conversely, if all `n` nodes are processed, their removal order is a valid topological order, proving the graph has no directed cycle.

**Dynamic-programming correctness.** When node `i` is processed, all predecessors have propagated because its indegree is zero. For each color, `dp[i]` is therefore the maximum over every path ending through every predecessor, with node `i` counted if its color matches. Every path ending at `i` must use one of those predecessor edges or begin at `i` if it is a source. Induction over topological order proves the state is exact. Taking the maximum state value over processed nodes yields the largest path color value.

## Complexity detail

Let `n` be nodes and `m` be edges. Graph construction takes `O(n + m)`. Every node enters and leaves the queue once. Every edge performs 26 dynamic-programming updates, so total time is `O(26(n + m))`, conventionally linear because 26 is fixed.

The adjacency lists use `O(n + m)` storage, indegrees and queue use `O(n)`, and `dp` contains `26n` integers. Total space is `O(26n + m)`.

## Alternatives and edge cases

- **Depth-first search with memoization:** It can compute the same color vectors and detect recursion-stack cycles, but recursion depth near 100,000 is risky in Python.
- **One DP value per node:** Tracking only the node’s own color loses paths where another color becomes dominant later; all 26 counts are required.
- **No edges:** Every node is a one-node path, all are sources, and the answer is one.
- **Self-loop:** Its node never reaches indegree zero, so `cnt < n` and minus one is returned.
- **Cycle plus acyclic component:** Some nodes may be processed, but any unprocessed cycle forces the final minus one.
- **Several predecessors:** `max` merges the best path for each color independently.
- **Several sources:** Each receives its own color count one and enters the initial queue.
- **Parallel edges if present:** Each increments and later decrements indegree; repeated propagation is harmless because maximum is idempotent.
- **Destination color increment:** The added Boolean depends on `colors[j]`, not the predecessor’s color.
- **Answer initialization:** One is valid because `n >= 1`, including an isolated graph.
- **Topological timing:** A node is enqueued only after all predecessor contributions have been applied.
- **Fixed alphabet:** The factor 26 is constant but remains explicit in memory and operation counts.
