# Tree of Coprimes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1766 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Tree, Depth-First Search, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-of-coprimes/) |

## Problem Description

### Goal

A connected, undirected, acyclic graph contains $n$ nodes numbered from $0$ through $n-1$ and is rooted at node $0$. The array `nums` assigns a positive integer value to each node, and every pair in `edges` joins two nodes of the tree.

Two values are coprime when their greatest common divisor is $1$. An ancestor of node `i` is another node on the unique shortest path from `i` to the root; a node is not its own ancestor.

For every node, find its closest ancestor whose value is coprime with the node's value. Return `-1` for a node having no such ancestor.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 50$.
- `edges`: exactly $n-1$ pairs `[u, v]`, each joining distinct node indices with $0 \le u,v<n$.
- Together, the edges form one connected tree rooted at node `0`.

**Return value**

- Return an integer array `answer` of length $n$.
- `answer[i]` is the index of the deepest proper ancestor of node `i` whose value has greatest common divisor $1$ with `nums[i]`, or `-1` if no such ancestor exists.

### Examples

**Example 1**

- Input: `nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]`
- Output: `[-1,0,0,1]`
- Explanation: Node `2` skips its value-`3` parent and uses node `0`; node `3` is coprime with its parent.

**Example 2**

- Input: `nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]`
- Output: `[-1,0,-1,0,0,0,-1]`
- Explanation: Each entry selects the nearest qualifying node on that node's path to root `0`.

**Example 3**

- Input: `nums = [7], edges = []`
- Output: `[-1]`
- Explanation: The root has no proper ancestors.
