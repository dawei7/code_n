# First Completely Painted Row or Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2661 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/first-completely-painted-row-or-column/) |

## Problem Description

### Goal

You are given a 0-indexed array `arr` and an $m \times n$ matrix `mat`. Each contains every integer from $1$ through $mn$ exactly once. Process `arr` from left to right; at index `i`, paint the unique matrix cell whose value is `arr[i]`.

Return the smallest index `i` at which all cells of at least one matrix row or at least one matrix column have been painted. A row and a column may become complete on the same operation, but the requested result is still that single earliest array index.

### Function Contract

**Inputs**

- `arr`: A permutation of the integers from $1$ through $mn$ describing paint order.
- `mat`: An $m \times n$ matrix containing the same values exactly once, where $1 \le m,n \le 10^5$ and $1 \le mn \le 10^5$.

**Return value**

- Return the earliest 0-based index in `arr` that completes a row or column.

### Examples

#### Example 1

- **Input:** `arr = [1,3,4,2], mat = [[1,4],[2,3]]`
- **Output:** `2`
- **Explanation:** Painting value `4` at index `2` completes the first row and the second column.

#### Example 2

- **Input:** `arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]`
- **Output:** `3`
- **Explanation:** Painting value `4` completes the matrix's second column.
