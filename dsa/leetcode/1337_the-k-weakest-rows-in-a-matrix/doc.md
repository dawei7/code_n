# The K Weakest Rows in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1337 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) |

## Problem Description
### Goal
An $m\times n$ binary matrix represents soldiers with 1 and civilians with 0. Within every row, all soldiers stand before all civilians, so each row consists of a prefix of 1s followed by a suffix of 0s.

Row $i$ is weaker than row $j$ when it has fewer soldiers. If their soldier counts are equal, the row with the smaller index is weaker.

Return the indices of the `k` weakest rows, ordered from weakest to strongest under that comparison.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ binary matrix, where $2\le m,n\le100$, and every row has all its 1s before its 0s.
- `k`: the number of row indices to return, where $1\le k\le m$.

**Return value**

An array containing exactly the `k` weakest row indices in increasing strength order, breaking equal-strength ties by smaller index.

### Examples
**Example 1**

- Input: `mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]`, `k = 3`
- Output: `[2,0,3]`

**Example 2**

- Input: `mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]`, `k = 2`
- Output: `[0,2]`

**Example 3**

- Input: `mat = [[0,0],[0,0],[1,1]]`, `k = 2`
- Output: `[0,1]`
- Explanation: Rows 0 and 1 both contain no soldiers, so their indices decide their order.
