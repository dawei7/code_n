# Kth Ancestor of a Tree Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1483 |
| Difficulty | Hard |
| Topics | Binary Search, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) |

## Problem Description
### Goal

A rooted tree contains `n` nodes numbered from `0` through `n - 1`. It is supplied as a `parent` array: `parent[i]` gives the direct parent of node `i`, and node `0` is the root with `parent[0] = -1`.

Build a `TreeAncestor` object that answers repeated ancestor queries. For `getKthAncestor(node, k)`, follow the path from `node` toward the root and return the node reached after exactly `k` parent steps. If that many ancestors do not exist, return `-1`.

### Function Contract
**Inputs**

Let $Q$ be the number of calls to `getKthAncestor`.

- Constructor `TreeAncestor(n, parent)`:
  - `n`: the node count, with $1 \le n \le 5 \cdot 10^4$.
  - `parent`: an array of length $n$ with `parent[0] = -1`.
  - For every $1 \le i < n$, $0 \le \texttt{parent[i]} < n$; the array describes a rooted tree whose root is node `0`.
- Method `getKthAncestor(node, k)`:
  - `node`: a node identifier with $0 \le \texttt{node} < n$.
  - `k`: the requested ancestor distance, with $1 \le k \le n$.
- At most $5 \cdot 10^4$ queries are issued.
- The app-local `solve(n, parent, operations)` receives calls as `["getKthAncestor", [node, k]]` and returns one result per call.

**Return value**

Each query returns the node exactly `k` edges above `node`, or `-1` if the path reaches above the root. The app-local wrapper returns these query results in operation order.

### Examples
**Example 1**

- Constructor: `TreeAncestor(7, [-1,0,0,1,1,2,2])`
- Operations: `getKthAncestor(3, 1)`, `getKthAncestor(5, 2)`, `getKthAncestor(6, 3)`
- Output: `[1,0,-1]`
- Explanation: Node `3` has parent `1`; node `5` reaches root `0` in two steps; node `6` has depth two, so a third ancestor does not exist.
