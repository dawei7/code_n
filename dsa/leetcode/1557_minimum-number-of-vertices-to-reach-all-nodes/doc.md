# Minimum Number of Vertices to Reach All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1557 |
| Difficulty | Medium |
| Topics | Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) |

## Problem Description
### Goal

You are given a directed acyclic graph with `n` vertices numbered from `0` through `n - 1`. Each pair `[from, to]` in `edges` is a distinct directed edge from `from` to `to`.

Choose the smallest set of starting vertices such that every graph vertex is reachable from at least one chosen vertex. A starting vertex counts as reachable from itself. The contract guarantees that the minimum set is unique, although its vertices may be returned in any order.

### Function Contract
**Inputs**

- `n`: The number of vertices, with $2 \le n \le 10^5$.
- `edges`: A nonempty list of $M$ distinct directed pairs, where $1 \le M \le \min(10^5, n(n-1)/2)$. Every endpoint lies in $[0,n-1]$, and all edges together form a directed acyclic graph.

**Return value**

Return the unique minimum set of vertices from which all `n` vertices are reachable. The output order is unrestricted.

### Examples
**Example 1**

- Input: `n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]`
- Output: `[0,3]`

**Example 2**

- Input: `n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]`
- Output: `[0,2,3]`

**Example 3**

- Input: `n = 4, edges = [[0,1],[1,2],[2,3]]`
- Output: `[0]`

### Required Complexity

- **Time:** $O(n+M)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Identify the vertices that no other start can reach**

A vertex with indegree zero has no incoming edge. No path beginning at a different vertex can enter it, so every valid starting set must contain that vertex. This makes every zero-indegree vertex mandatory.

Conversely, consider a vertex with at least one incoming edge. Follow one incoming edge backward, and continue doing so while the current vertex still has a predecessor. Because the graph is finite and acyclic, this backward walk cannot revisit a vertex and must eventually stop at a zero-indegree vertex. Reversing the collected edges gives a directed path from that mandatory source to the original vertex. Thus all vertices are reachable from the zero-indegree vertices, and no additional start is necessary.

Together, necessity and sufficiency show that the unique minimum set is exactly the set of vertices with indegree zero.

**Record only whether an incoming edge exists**

The exact indegree count is unnecessary. Allocate one Boolean flag per vertex, scan every edge once, and mark its destination. A final scan returns every unmarked vertex. Iterating vertices in numeric order provides deterministic output even though the contract accepts any order.

#### Complexity detail

Initializing and scanning the $n$ flags takes $O(n)$ time, while processing the $M$ edges takes $O(M)$ time. The total is $O(n+M)$.

The Boolean array occupies $O(n)$ auxiliary space. The returned source list can itself contain up to $n-1$ vertices under the nonempty-edge constraint, so including output storage does not change the $O(n)$ bound.

#### Alternatives and edge cases

- **Indegree counters:** increment a numeric counter for each destination and return the zero entries. This is equally correct and has the same bounds, but Boolean presence is all the result requires.
- **Destination hash set:** collect all edge destinations and return vertices absent from the set. This is concise and expected $O(n+M)$, with hash-table rather than dense-array storage.
- **Traversal from candidate starts:** repeatedly run DFS or BFS to test which starts are needed. It performs work the indegree characterization makes unnecessary and can become quadratic.
- **Topological sorting:** Kahn's algorithm initially discovers the same zero-indegree vertices, but processing the rest of the queue adds no information needed for this task.
- **Disconnected components:** each component's zero-indegree source vertices are included automatically; weak or directed connectivity is not assumed.
- **Multiple predecessors:** a vertex is excluded as soon as any incoming edge exists; its exact number of predecessors does not matter.
- **Long chain:** only the first vertex has indegree zero, so a chain returns one start.
- **Several sources converging:** all source vertices remain mandatory even when their paths later merge.

</details>
