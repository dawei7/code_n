# Maximum Path Quality of a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2065 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-path-quality-of-a-graph/) |

## Problem Description

### Goal

An undirected graph has $n$ nodes numbered from $0$ through $n-1$. Each node has a nonnegative value, and every edge has a positive travel time. An edge may be traversed in either direction, and the graph need not be connected.

A valid path starts at node $0$, ends at node $0$, and uses at most `maxTime` seconds. Nodes and edges may be visited repeatedly. The path's quality is the sum of the values of its distinct visited nodes, so returning to a node never adds its value again.

Return the greatest quality among all valid paths. Each node has degree at most four, edge travel times are at least $10$, and `maxTime` is at most $100$.

### Function Contract

**Inputs**

- `values`: an array of $n$ node values, where $1 \le n \le 1000$ and each value lies between $0$ and $10^8$.
- `edges`: an array of $e$ unique undirected edges `[u,v,time]`, where $0 \le e \le 2000$, every travel time is between $10$ and $100$, and each node has degree at most four.
- `maxTime`: the inclusive route-time budget, where $10 \le \texttt{maxTime} \le 100$.

Let $L$ be the maximum number of edges any route within the time budget can traverse. Because every edge costs at least $10$, $L \le 10$.

**Return value**

- Return the maximum sum of distinct node values along a route that starts and finishes at node $0$ within the budget.

### Examples

**Example 1**

- Input: `values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49`
- Output: `75`
- Explanation: The route `0 -> 1 -> 0 -> 3 -> 0` takes $40$ seconds and collects nodes $0$, $1$, and $3$.

**Example 2**

- Input: `values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30`
- Output: `25`
- Explanation: Visiting node $3$ and returning takes $20$ seconds and collects values $5+20$.

**Example 3**

- Input: `values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50`
- Output: `7`
- Explanation: The route `0 -> 1 -> 3 -> 1 -> 0` takes $46$ seconds and counts nodes $0$, $1$, and $3$ once each.

### Required Complexity

- **Time:** $O(n+e+4^L)$
- **Space:** $O(n+e+L)$

<details>
<summary>Approach</summary>

#### General

**Bounded walks make exhaustive search practical**

Build an adjacency list for the undirected graph. A depth-first search state contains the current node, elapsed time, current quality, and visit counts. From that state, try every incident edge whose travel time keeps the route within `maxTime`. The degree limit gives at most four choices per step, while the minimum edge time bounds the depth by $L \le 10$.

**Count a node only on entry to the visited set**

Before following an edge, increment the destination's visit count. Add its value to the running quality only when that count changes from zero to one. After the recursive call, decrement the count to restore the previous path state. Whenever the current node is $0$, the explored prefix is itself a valid return route, so use its quality to update the answer; exploration may continue if time remains.

The search enumerates every edge sequence whose total time fits the budget because it branches over every legal next edge. Visit counts make the maintained quality equal to the sum of exactly the distinct nodes on that sequence. Every valid path is therefore considered at its return to node $0$, and taking the greatest recorded quality produces the optimum.

#### Complexity detail

Building the graph takes $O(n+e)$ time and space. With branching factor at most four and at most $L$ traversals, DFS visits $O(4^L)$ states, giving $O(n+e+4^L)$ total time. The adjacency list, visit-count array, and recursion stack use $O(n+e+L)$ space. The contract fixes $L \le 10$, but retaining $L$ shows the bounded exponential search explicitly.

#### Alternatives and edge cases

- **Recompute quality from the whole path:** This remains correct, but scanning all node visit counts at return states adds an avoidable factor of $n$.
- **Bitmask dynamic programming:** A mask can represent distinct visits only when the relevant node count is small; the graph may contain up to $1000$ nodes.
- **Shortest-return pruning:** Precomputing each node's shortest distance to node $0$ can prune states that cannot return in time, improving constants without changing the worst-case bound.
- The zero-length route at node $0$ is always valid and includes `values[0]`.
- A high-value node is useless when the remaining time cannot cover both reaching it and returning.
- Revisiting a node or edge is allowed and may be necessary to return, but a node's value is added only once.
- Disconnected nodes never affect the result.
- A route using exactly `maxTime` seconds is valid.

</details>
