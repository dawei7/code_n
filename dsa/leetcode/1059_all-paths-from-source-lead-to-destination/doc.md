# All Paths from Source Lead to Destination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) |

## Problem Description

### Goal

An array `edges` describes a directed graph: each pair `[a, b]` is an edge from node `a` to node `b`. Given nodes `source` and `destination`, decide whether all paths beginning at `source` eventually end at `destination`.

This condition requires at least one path from `source` to `destination`. Every terminal node reachable from `source` must be `destination`, and the number of possible paths from `source` to `destination` must be finite. Thus, a reachable dead end other than `destination` or a reachable cycle makes the answer false. Return true if and only if all paths satisfy these requirements.

### Function Contract

**Inputs**

- `n`: the number of nodes, labeled from `0` through `n - 1`, where $1 \le n \le 10^4$.
- `edges`: at most $10^4$ directed pairs `[a, b]`; self-loops and parallel edges are allowed.
- `source`: the node at which every considered path starts.
- `destination`: the node at which every path must terminate.
- Let $V=n$ and let $E$ be the number of edges.

**Return value**

- `true` exactly when every path from `source` eventually ends at `destination`; otherwise `false`.

### Examples

**Example 1**

- Input: `n = 3, edges = [[0, 1], [0, 2]], source = 0, destination = 2`
- Output: `false`
- Explanation: Node 1 is a reachable terminal node different from the destination.

**Example 2**

- Input: `n = 4, edges = [[0, 1], [0, 3], [1, 2], [2, 1]], source = 0, destination = 3`
- Output: `false`
- Explanation: One route reaches node 3, but another can loop forever between nodes 1 and 2.

**Example 3**

- Input: `n = 4, edges = [[0, 1], [0, 2], [1, 3], [2, 3]], source = 0, destination = 3`
- Output: `true`

### Required Complexity

- **Time:** $O(V+E)$
- **Space:** $O(V+E)$

<details>
<summary>Approach</summary>

#### General

**Reject an invalid destination:** A path must end when it reaches `destination`, so `destination` cannot have outgoing edges. Build an adjacency list and reject immediately if it does.

**Classify only reachable nodes:** Perform depth-first search from `source` with three states: unseen, visiting, and safe. A visiting node is on the current DFS path. Encountering it again reveals a reachable cycle, which permits infinitely many paths. A node with no outgoing edges is safe only when it is `destination`; any other reachable terminal node violates the requirement.

**Memoize completed subgraphs:** After all outgoing neighbors of a node are safe, mark the node safe. Any later edge to it can reuse that result. An explicit stack stores each node and the index of its next neighbor, avoiding recursion-depth failure on a chain of up to $10^4$ nodes.

Every rejected situation directly supplies a forbidden path: a wrong terminal, a cycle, or an outgoing edge from the destination. Conversely, if the search finishes, every reachable node has been proved safe. Following any edge then moves through safe nodes in an acyclic reachable subgraph and must terminate; the terminal-node rule makes that endpoint `destination`.

#### Complexity detail

Building adjacency lists takes $O(V+E)$ time and space. Each reachable node changes state a constant number of times and each outgoing edge is examined once, so DFS takes $O(V+E)$ time. The state array and explicit stack use $O(V)$ space in addition to the $O(V+E)$ graph.

#### Alternatives and edge cases

- **Recursive three-color DFS:** It has the same asymptotic cost and proof, but a path with thousands of nodes can exceed Python's recursion limit.
- **Rescan the edge list:** Finding each node's neighbors by scanning all edges avoids adjacency lists but can cost $O(VE)$ time.
- **Reverse topological elimination:** It can identify nodes whose paths all reach the destination, but needs careful reachable-subgraph and terminal handling.
- **Unreachable cycle:** It does not matter because no path beginning at `source` can enter it.
- **Self-loop or reachable directed cycle:** It makes the number of possible paths infinite, so return `false`.
- **Parallel edges:** They do not change validity and are safely examined as separate adjacency entries.
- **Source equals destination:** The answer is true only when that node has no outgoing edges.
- **Wrong dead end:** Any reachable node with no outgoing edges other than `destination` makes the answer false.

</details>
