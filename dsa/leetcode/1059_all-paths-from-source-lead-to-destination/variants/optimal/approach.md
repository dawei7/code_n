## General
**Reject an invalid destination:** A path must end when it reaches `destination`, so `destination` cannot have outgoing edges. Build an adjacency list and reject immediately if it does.

**Classify only reachable nodes:** Perform depth-first search from `source` with three states: unseen, visiting, and safe. A visiting node is on the current DFS path. Encountering it again reveals a reachable cycle, which permits infinitely many paths. A node with no outgoing edges is safe only when it is `destination`; any other reachable terminal node violates the requirement.

**Memoize completed subgraphs:** After all outgoing neighbors of a node are safe, mark the node safe. Any later edge to it can reuse that result. An explicit stack stores each node and the index of its next neighbor, avoiding recursion-depth failure on a chain of up to $10^4$ nodes.

Every rejected situation directly supplies a forbidden path: a wrong terminal, a cycle, or an outgoing edge from the destination. Conversely, if the search finishes, every reachable node has been proved safe. Following any edge then moves through safe nodes in an acyclic reachable subgraph and must terminate; the terminal-node rule makes that endpoint `destination`.

## Complexity detail
Building adjacency lists takes $O(V+E)$ time and space. Each reachable node changes state a constant number of times and each outgoing edge is examined once, so DFS takes $O(V+E)$ time. The state array and explicit stack use $O(V)$ space in addition to the $O(V+E)$ graph.

## Alternatives and edge cases
- **Recursive three-color DFS:** It has the same asymptotic cost and proof, but a path with thousands of nodes can exceed Python's recursion limit.
- **Rescan the edge list:** Finding each node's neighbors by scanning all edges avoids adjacency lists but can cost $O(VE)$ time.
- **Reverse topological elimination:** It can identify nodes whose paths all reach the destination, but needs careful reachable-subgraph and terminal handling.
- **Unreachable cycle:** It does not matter because no path beginning at `source` can enter it.
- **Self-loop or reachable directed cycle:** It makes the number of possible paths infinite, so return `false`.
- **Parallel edges:** They do not change validity and are safely examined as separate adjacency entries.
- **Source equals destination:** The answer is true only when that node has no outgoing edges.
- **Wrong dead end:** Any reachable node with no outgoing edges other than `destination` makes the answer false.
