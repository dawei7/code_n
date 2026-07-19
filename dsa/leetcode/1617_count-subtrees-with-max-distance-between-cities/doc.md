# Count Subtrees With Max Distance Between Cities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1617 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Bit Manipulation, Tree, Dynamic Programming, Bitmask, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) |

## Problem Description
### Goal
There are `n` cities numbered from 1 through `n`, joined by `n - 1` bidirectional edges. A unique path exists between every pair of cities, so the complete infrastructure is a tree. A subtree is determined by a subset of cities whose induced paths remain entirely inside that subset; equivalently, the selected cities form a connected induced subgraph. Two subtrees differ when their selected city sets differ.

For every distance $d$ from 1 through $n-1$, count the subtrees whose maximum distance between any two selected cities is exactly $d$. Distance is measured by the number of edges on the unique path. Return the $n-1$ counts in increasing distance order. Single-city subsets have diameter zero and therefore do not contribute to the returned array.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 15$.
- `edges`: exactly $n-1$ distinct pairs `[u, v]` describing a tree on cities 1 through `n`.

**Return value**

Return an array `answer` of length $n-1$, where `answer[d - 1]` is the number of connected city subsets with diameter exactly $d$.

### Examples
**Example 1**

- Input: `n = 4, edges = [[1,2],[2,3],[2,4]]`
- Output: `[3,4,0]`

**Example 2**

- Input: `n = 2, edges = [[1,2]]`
- Output: `[1]`

**Example 3**

- Input: `n = 3, edges = [[1,2],[2,3]]`
- Output: `[2,1]`
