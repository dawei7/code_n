# Sort the Matrix Diagonally

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1329 |
| Difficulty | Medium |
| Topics | Array, Sorting, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-the-matrix-diagonally/) |

## Problem Description
### Goal
In a matrix, a diagonal begins in either the top row or the leftmost column and continues one row down and one column right until it reaches an edge. Cells belong to the same such diagonal exactly when their row-minus-column difference is equal.

Given an integer matrix `mat`, sort the values on every top-left-to-bottom-right diagonal independently in ascending order. Values must remain on their original diagonal; only their order along that diagonal changes.

Return the resulting matrix. Diagonals of length one and diagonals whose values are already ascending remain unchanged.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ integer matrix, where $1\le m,n\le100$ and $1\le\texttt{mat[i][j]}\le100$.

Let $L=\min(m,n)$ be the maximum diagonal length.

**Return value**

The matrix after each diagonal has been independently sorted in ascending order from its top-left end toward its bottom-right end.

### Examples
**Example 1**

- Input: `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`
- Output: `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`

**Example 2**

- Input: `mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]`
- Output: `[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]`

**Example 3**

- Input: `mat = [[2,1],[1,2]]`
- Output: `[[2,1],[1,2]]`
- Explanation: Every diagonal is already ascending.

### Required Complexity
- **Time:** $O(mn\log L)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Group cells by a stable diagonal key**

Moving from `(row, column)` to `(row + 1, column + 1)` preserves `row - column`, so use that difference as the key for a list of diagonal values. Scan the matrix once and append every value to its key's list.

Sort each list in descending order. Then scan matrix cells again in normal row-major order and replace each cell by popping from the end of its diagonal list. Row-major order encounters cells of a fixed diagonal from top-left to bottom-right, while each pop returns the smallest remaining value. Consequently every diagonal is written back in ascending order and no value crosses to another diagonal.

The grouping partitions all cells by their unique difference key, sorting preserves each group's multiset, and the second traversal assigns that multiset in the required order. These facts establish both value preservation and the ordering condition.

#### Complexity detail

There are $mn$ stored values. Sorting a diagonal of length at most $L$ costs $O(k\log k)$ for its length $k$; summed across diagonals, this is bounded by $O(mn\log L)$. The groups collectively store $mn$ values, so auxiliary space is $O(mn)$.

#### Alternatives and edge cases

- **Counting sort per diagonal:** Since values lie between 1 and 100, frequency arrays can reduce sorting to $O(mn)$ time, but the comparison-sort grouping is more general.
- **Sort from each boundary start:** Extracting, sorting, and replacing each diagonal directly uses only $O(L)$ temporary space and the same comparison-sort time bound.
- **Selection sort each diagonal:** It avoids a library sort but can take $O(mnL)$ time.
- **One row or one column:** Every diagonal contains one cell, so the matrix is unchanged.
- **Duplicate values:** They remain duplicated and their relative identity is irrelevant.
- **Rectangular matrices:** Top-row and left-column starts together cover every diagonal exactly once.

</details>
