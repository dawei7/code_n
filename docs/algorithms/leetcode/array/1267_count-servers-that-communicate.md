# Count Servers that Communicate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1267 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting |
| Official Link | [count-servers-that-communicate](https://leetcode.com/problems/count-servers-that-communicate/) |

## Problem Description & Examples
### Goal
Count servers that can communicate with at least one other server in the same row or column.

### Function Contract
**Inputs**

- `grid`: binary matrix where `1` is a server and `0` is empty.

**Return value**

The number of communicating servers.

### Examples
**Example 1**

- Input: `grid = [[1,0],[0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,0],[1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Row and column counting.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m + n)`
