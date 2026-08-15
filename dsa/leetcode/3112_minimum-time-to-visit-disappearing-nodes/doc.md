# Minimum Time to Visit Disappearing Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3112 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-time-to-visit-disappearing-nodes](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) |

## Problem Description

### Goal

An undirected graph has $n$ nodes numbered from $0$ through $n-1$. Each entry `[u, v, length]` in `edges` creates an edge between `u` and `v` that takes `length` units of time to traverse. The graph may be disconnected, and multiple edges may connect the same pair of nodes.

For every node $i$, `disappear[i]` is the instant when that node vanishes and can no longer be visited. Starting at node $0$ at time $0$, find the minimum arrival time for every node. An arrival is valid only when it is strictly earlier than the destination's disappearance time; arriving exactly when it disappears is too late. Return $-1$ for every node that cannot be reached under this rule.

### Function Contract

Let $m$ be the number of entries in `edges`.

**Inputs**

- `n`: The number of nodes, where $1 \le n \le 5\cdot10^4$.
- `edges`: A list of $m$ undirected weighted edges `[u, v, length]`, where $0 \le m \le 10^5$, $0 \le u,v < n$, and $1 \le \texttt{length} \le 10^5$.
- `disappear`: A length-$n$ list with $1 \le \texttt{disappear[i]} \le 10^5$.

**Return value**

- A length-$n$ list whose entry at index $i$ is the minimum valid arrival time from node $0$, or $-1$ when node $i$ is unreachable before disappearing.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]`
- **Output:** `[0,-1,4]`
- **Explanation:** Node $1$ disappears before time $2$, so the route through it is invalid; node $2$ is reached directly at time $4$.

#### Example 2

- **Input:** `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]`
- **Output:** `[0,2,3]`
- **Explanation:** Node $1$ is reached before time $3$, enabling the shorter arrival at node $2$.

#### Example 3

- **Input:** `n = 2, edges = [[0,1,1]], disappear = [1,1]`
- **Output:** `[0,-1]`
- **Explanation:** Reaching node $1$ at time $1$ is invalid because it disappears at that exact time.
