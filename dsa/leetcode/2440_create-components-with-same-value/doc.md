# Create Components With Same Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2440 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Tree, Depth-First Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Create Components With Same Value](https://leetcode.com/problems/create-components-with-same-value/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes labeled from 0 through $n-1$. The 0-indexed array `nums` assigns `nums[i]` to node $i$, and each pair `[a, b]` in `edges` connects nodes `a` and `b`.

You may delete some tree edges, producing several connected components. Define a component's value as the sum of the values on all nodes belonging to it. Return the maximum number of edges that can be deleted while making every resulting component have exactly the same value.

### Function Contract

**Inputs**

- `nums`: A length-$n$ list of node values, where $1 \le n \le 2\cdot10^4$ and $1 \le \texttt{nums[i]} \le 50$.
- `edges`: The $n-1$ undirected edges of a valid tree, with endpoints from 0 through $n-1$.

**Return value**

- The greatest number of edges whose deletion leaves equal-value connected components.

### Examples

**Example 1**

- Input: `nums = [6, 2, 2, 2, 6], edges = [[0, 1], [1, 2], [1, 3], [3, 4]]`
- Output: `2`
- Explanation: Delete `[0, 1]` and `[3, 4]`. The components `{0}`, `{1, 2, 3}`, and `{4}` each have value 6.

**Example 2**

- Input: `nums = [2], edges = []`
- Output: `0`
- Explanation: A one-node tree has no edge available to delete.
