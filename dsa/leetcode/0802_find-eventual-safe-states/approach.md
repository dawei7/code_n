## General

**Characterize safety through outgoing neighbors**

A terminal node is safe because every path starting there ends immediately.

A nonterminal node is safe exactly when every one of its outgoing neighbors is safe. If even one edge leads toward a cycle, choosing that edge creates a path that never has to reach a terminal node, so the source is unsafe.

This suggests starting with known terminal nodes and repeatedly marking any node whose outgoing choices have all become known safe.

**Reverse edges to move from a safe node to its predecessors**

The input graph lists outgoing neighbors. Once node `j` is proven safe, the algorithm needs to find every node `i` that points to `j` so it can remove that now-resolved outgoing dependency.

Dictionary `rg` stores the reversed graph:

`rg[j].append(i)`

for every original edge `i -> j`.

Thus `rg[j]` is the list of original predecessors that may become safe after `j` is resolved.

**Interpret `indeg` carefully**

Despite its name, `indeg[i]` is not the original graph's incoming-edge count. The code assigns:

`indeg[i] = len(graph[i])`.

It is the number of outgoing edges from `i` that have not yet been proven to lead to safe nodes.

Calling it a remaining-outdegree counter makes the algorithm easier to understand. Initially every outgoing edge is unresolved. Each time a successor becomes safe, one counter is removed from each predecessor.

**Initialize with terminal nodes**

Nodes whose original adjacency lists are empty have remaining count zero. The deque comprehension places all such nodes in `q`.

These are the base safe states. They need no assumptions about other nodes.

If several terminal nodes exist, their relative queue order does not matter. Each will propagate safety independently through reversed edges.

**Remove resolved safe edges**

When node `i` is popped, it is safe. For every original predecessor `j` in `rg[i]`, the edge `j -> i` can no longer be a route to a cycle.

The method decrements:

`indeg[j] -= 1`.

If that count reaches zero, every outgoing neighbor of `j` has now been popped as safe. Therefore every path from `j` moves into a safe node, so `j` is safe and enters the queue.

A node is enqueued only when its counter changes to zero, so it is processed at most once.

**Why cycles never enter the queue**

Every node in a directed cycle has at least one outgoing edge to the next cycle node. None of those cycle nodes can be established from a terminal base case, so that cycle edge is never removed.

Their remaining counters stay positive. Any node with a path to the cycle also retains at least one unresolved edge along a route leading toward it.

Therefore the reverse elimination process excludes exactly cycle nodes and all nodes that can choose a path into a cycle.

**Self-loops are handled naturally**

A self-loop `i -> i` adds `i` to `rg[i]` and contributes one to `indeg[i]`.

The node cannot begin with count zero. It cannot be popped to remove its own loop because popping would first require the loop to be resolved. Thus it remains unsafe, as required.

**Trace the first example**

For `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`, nodes five and six start with zero outgoing edges and enter the queue.

Popping five removes dependencies from nodes two and four. Each has no other outgoing edge, so their counters reach zero and they enter the queue.

Popping two and four may reduce other predecessors, but nodes zero, one, and three retain dependencies participating in or leading toward the cycle `0 -> 1 -> 3 -> 0`.

The nodes with final zero counters are two, four, five, and six.

**Why the final list is already sorted**

Queue order is determined by propagation, not numeric order. The algorithm does not return the pop sequence.

Instead it scans `indeg` with `enumerate` from index zero upward and selects entries equal to zero:

`[i for i, v in enumerate(indeg) if v == 0]`.

All safe nodes have zero final counters, and indices are visited ascending, so the result satisfies the sorting requirement without an extra $O(V\log V)$ sort.

**The elimination invariant**

At every point, `indeg[u]` equals the number of outgoing edges from `u` whose destination has not yet been removed as a proven safe node.

Initialization counts all outgoing edges. Popping safe `i` removes exactly one corresponding unresolved edge from every predecessor. No other counter changes.

When a count reaches zero, all outgoing destinations are proven safe, which proves the predecessor safe. This maintains the invariant and queue meaning.

**Why every processed node is safe**

Terminal nodes are safe. Any later queued node has all outgoing edges to nodes already proven safe.

Following any path from it enters one of those safe nodes and then necessarily terminates. Induction on queue insertion order proves every processed node is safe.

**Why every safe node is processed**

Consider a safe node. It cannot reach a cycle. The reachable subgraph from it is finite and acyclic, so every sufficiently long path reaches a terminal node.

Reverse elimination starts at those terminals. Working backward through the acyclic reachable portion eventually removes every successor dependency of the safe node, reducing its counter to zero. Thus it is queued.

Final zero counters therefore identify exactly all eventual safe states.

## Complexity detail

Let $V$ be the number of nodes and $E$ the number of directed edges. Building the reverse graph and remaining-outdegree counts examines each node and edge once. Queue processing removes each reverse edge once, and the final scan visits each node once. Total time is $O(V+E)$.

The reverse adjacency lists use $O(V+E)$ space, while the count array and queue use $O(V)$. Total auxiliary space is $O(V+E)$.

## Alternatives and edge cases

- **Three-color depth-first search:** Mark nodes unvisited, active, or confirmed safe. It also takes $O(V+E)$ but uses recursion or an explicit stack.

- **Run cycle detection independently from every node:** It repeats work and can become quadratic without memoized states.

- **Return queue order:** Incorrect for the required ascending output; scan node indices afterward.

- **Terminal node:** It starts safe with remaining count zero.

- **Self-loop:** Its unresolved edge prevents it from entering the queue.

- **Cycle with an exit to a terminal:** It is still unsafe because some possible path can stay in the cycle.

- **Node with one safe and one unsafe successor:** Its counter never reaches zero, matching the “every path” requirement.

- **Disconnected graph:** Every component is handled through its own terminal propagation or unresolved cycles.

- **Misleading variable name:** `indeg` stores original remaining outdegree, not ordinary indegree.
