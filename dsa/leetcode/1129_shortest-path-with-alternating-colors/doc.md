# Shortest Path with Alternating Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1129 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-path-with-alternating-colors/) |

## Problem Description

### Goal

You are given a directed graph with `n` nodes labeled from `0` through `n - 1`. Every edge is either red or blue, and the graph may contain self-edges and parallel edges. Each `redEdges[i] = [a,b]` represents a directed red edge from `a` to `b`, while each `blueEdges[j] = [u,v]` represents a directed blue edge from `u` to `v`.

Return an array `answer` of length `n`. For every node `x`, `answer[x]` must be the length of the shortest directed path from node `0` to node `x` whose consecutive edges alternate colors. Either color may be used for the first edge. If no alternating path reaches `x`, set `answer[x] = -1`; the empty path makes `answer[0] = 0`.

### Function Contract

**Inputs**

- `n`: the number of nodes, where $1 \le n \le 100$.
- `redEdges`: a list of $r$ directed red edges, where $0 \le r \le 400$ and every endpoint lies in $[0,n-1]$.
- `blueEdges`: a list of $b$ directed blue edges, where $0 \le b \le 400$ and every endpoint lies in $[0,n-1]$.

**Return value**

An integer array of length $n$ containing each shortest alternating-path length from node `0`, or `-1` when unreachable.

### Examples

**Example 1**

- Input: `n = 3, redEdges = [[0,1],[1,2]], blueEdges = []`
- Output: `[0,1,-1]`

**Example 2**

- Input: `n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]`
- Output: `[0,1,-1]`

### Required Complexity

- **Time:** $O(n + r + b)$
- **Space:** $O(n + r + b)$

<details>
<summary>Approach</summary>

#### General

**Make the last color part of the state.** Reaching the same node after red and after blue edges creates different futures: the first state may take only blue next, while the second may take only red. Build separate red and blue adjacency lists and run breadth-first search over states `(node, last_color)`.

**Allow either first color.** Put both `(0, red)` and `(0, blue)` into the queue at distance zero. These are conceptual starting states, not actual incoming edges. Expanding `(node, last_color)` follows only adjacency edges of the opposite color and produces states carrying that new color.

**Visit each color state once.** Breadth-first search processes states in nondecreasing path length. Therefore, the first time `(neighbor, next_color)` is reached, its distance is the shortest alternating distance for that exact state; later visits cannot improve it. The answer for a node is the smaller distance among its two color states, or `-1` if neither was reached. This state graph represents every alternating path and only alternating paths, so its BFS distances are exactly the required values.

#### Complexity detail

There are $2n$ color states. Each state is enqueued at most once, and each red or blue adjacency list is scanned only from the compatible state, so traversal takes $O(n + r + b)$ time. The adjacency lists, two-state distance table, and queue use $O(n + r + b)$ space.

#### Alternatives and edge cases

- **Repeated relaxation:** Bellman-Ford-style updates on the two-color state graph are correct, but scanning all edges for up to $2n$ rounds costs $O(n(r+b))$ time.
- **Visited nodes without color:** Marking only a node as visited can discard a later arrival with the opposite last color even though it enables a necessary continuation.
- **Self-edge:** It may change the last color while remaining at the same node, but only an unvisited color state needs to be enqueued.
- **Parallel edges:** Duplicate same-color edges do not change distances; the visited-state check prevents repeated work.
- **No outgoing path from zero:** The result is `0` for node `0` and `-1` for every other node.

</details>
