# Minimum Time to Collect All Apples in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1443 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) |

## Problem Description
### Goal

An undirected tree has $n$ vertices numbered from $0$ through $n-1$. Some
vertices contain an apple. Traversing either direction across one edge costs
one second, and any apple at a visited vertex is collected.

The journey must start at vertex $0$, collect every apple in the tree, and
return to vertex $0$. The array `edges` lists the tree's $n-1$ undirected
connections, while `hasApple[i]` states whether vertex `i` contains an
apple. Return the minimum total traversal time required for the complete
round trip.

### Function Contract
**Inputs**

- `n`: the number of vertices, where $1 \le n \le 10^5$.
- `edges`: a list of exactly $n-1$ pairs `[a, b]` describing an
  undirected tree on vertices $0$ through $n-1$.
- `hasApple`: a Boolean list of length $n$; `hasApple[i]` is true exactly
  when vertex `i` has an apple.

**Return value**

Return the minimum number of seconds needed to start at vertex $0$, collect
all apples, and finish again at vertex $0$.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, true, false, true, true, false]`
- Output: `8`
- Explanation: The required part of the tree contains four edges, each of
  which must be traversed once outward and once on the return.

**Example 2**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, true, false, false, true, false]`
- Output: `6`

**Example 3**

- Input: `n = 7, edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple = [false, false, false, false, false, false, false]`
- Output: `0`
