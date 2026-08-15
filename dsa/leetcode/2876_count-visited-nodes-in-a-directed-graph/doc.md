# Count Visited Nodes in a Directed Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2876 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Depth-First Search, Graph Theory, Topological Sort, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Visited Nodes in a Directed Graph](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/) |

## Problem Description

### Goal

A directed graph has $n$ nodes numbered from $0$ through $n-1$ and exactly $n$ directed edges. The 0-indexed array `edges` describes the graph: node $i$ has one outgoing edge leading to `edges[i]`.

For a chosen starting node $x$, visit $x$ and repeatedly follow the unique outgoing edge. Stop as soon as the process reaches a node that was already visited during this same traversal.

Return an array `answer` of length $n$ where `answer[i]` is the number of distinct nodes visited when the process starts from node $i$. Separate starting nodes may enter the same cycle or share part of their path, but each count belongs to its own traversal.

### Function Contract

**Inputs**

- `edges`: A list defining the unique outgoing neighbor of every node.

Let $n = \lvert\texttt{edges}\rvert$. The constraints are $2 \le n \le 10^5$, $0 \le \texttt{edges[i]} < n$, and `edges[i] != i` for every node $i$.

**Return value**

- A list of $n$ integers where position $i$ contains the number of distinct nodes encountered before the walk from $i$ repeats a node.

### Examples

#### Example 1

- **Input:** `edges = [1,2,0,0]`
- **Output:** `[3,3,3,4]`
- **Explanation:** Nodes $0$, $1$, and $2$ form a cycle of length $3$. Starting from node $3$ visits node $3$ before entering that cycle.

#### Example 2

- **Input:** `edges = [1,2,3,4,0]`
- **Output:** `[5,5,5,5,5]`
- **Explanation:** All five nodes form one directed cycle, so every starting point visits all five distinct nodes.
